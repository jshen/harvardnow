import unidecode
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
import re

# global lists for date information
month_days = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]
max_days = range(1, 32)
max_years = range(2007, datetime.now().year)

##############################
##      Movie Functions     ##
##############################

# used for getting current week overflow for february leap years
def isLeapYear(year):
    if year % 4 != 0:
        return 0
    elif year % 100 != 0:
        return 1
    elif year % 400 == 0:
        return 1
    else:
        return 0

# format info when given all the p elements in a table cell
def parseDay(day_info, month, year, find=None, info=False, results=[]):
    shows = ""
    try:
        date = day_info[0].getText()
        day_title = month + " " + date
        # get the text of the next element in the cell to check if it's empty
        next_text = day_info[1].getText()
        showtime = len(next_text)
        if "no screenings" in next_text.lower():
            showtime = 0
    except:
        showtime = 0
    if showtime > 1:
        # convert to a string to use datetime to check weekday of the date
        datetime_string = day_title + " " + str(year)
        time = datetime.strptime(datetime_string, "%B %d %Y")
        # look up for pretty printing
        weekday_num = time.weekday()
        weekday = weekdays[weekday_num]

        day_title = weekday + ", " + day_title + ":\n"

        shows += day_title 
        show_info = "  "

        # parse the information disincluding the date number
        day_shows = day_info[1:]
        for index, show in enumerate(day_shows):
            el_text = show.getText()
            if el_text:
                if show["class"][0] == "caltime":
                    show_info += el_text 
                    if show_info[len(show_info) - 1] == " ":
                        show_info = show_info[:-1] + ": "  
                    else:
                        show_info += ": "
                elif show["class"][0] == "calfilm":
                    show_info += '"' + el_text.strip() + '"'
                    if find and find.lower() in el_text.lower():
                        # basic search for full title
                        regex = r'  (.+): (.*' + find + '.*)'
                        match = re.search(regex, show_info, re.IGNORECASE) 
                        # convert with unicdecode to preserve special characters
                        show_title = unidecode.unidecode(match.group(2))
                        start_time = unidecode.unidecode(match.group(1))
                        result = "{0} is playing on {1}, {2} {3} at {4}.".format(
                            show_title, weekday, month, date, start_time)
                        if info:
                            # get soup for the info page
                            link = show.find("a")["href"]
                            full = "http://hcl.harvard.edu" + link
                            resp = urllib2.urlopen(full)
                            info_soup = BeautifulSoup(resp.read(), "lxml")

                            # get the title header
                            title = match.group(2)[1:-1] 
                            show_regex = re.compile('.*' + title + '.*', re.IGNORECASE)
                            info_soup = info_soup.find("body")
                            #try:
                            #    header = info_soup.find("h2", text=show_regex).parent
                            #except:
                            header = info_soup.find(text=show_regex)
                                    
                            if header:
                                # get info about movie relative to title
                                film_info = header.find_next("p")
                                if film_info.find("img"):
                                    film_info = film_info.find_next("p") 
                                description = unidecode.unidecode(film_info.find_next("p").getText())
                                film_info = unidecode.unidecode(film_info.getText()) + "\n"

                                film_info += description
                                film_info += "\n\nRead description at: " + full
                                results.append((result, film_info))
                        else:
                            results.append(result)
                    shows += show_info + "\n"
                    try:
                        next_el = day_shows[index + 1]
                        if next_el["class"][0] == "calnote":
                            shows += "    *" + next_el.getText() + "\n"
                    except:
                        pass
                    show_info = "  "

        shows += "\n"

    return shows, results

# get the shows playing on the current day
def getToday():
    resp = "Movies playing today:\n"
    now = datetime.now()
    day = now.day
    month_num = now.month
    month = months[month_num - 1]
    year = str(now.year)

    soup = getSoup(month, year)

    day_info = soup.find(text=str(day)).parent.parent
    day_info = day_info.find_all("p")

    info, dump = parseDay(day_info, month, year)
    resp += info
    return resp

# format the url for a calendar
def getSoup(month, year):
    month = month.lower()
    year = str(year)[-2::]
    url = "http://hcl.harvard.edu/hfa/calendar/{0}{1}.html".format(month, year)
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), "lxml")
    return soup

# get the shows within a week starting on a specified date, default today
def getWeek(day=None, month=None, year=None, find=None):
    now = datetime.now()
    if not day:
        day = now.day
    if not year:
        year = now.year

    if not month:
        month_num = now.month
        month = months[month_num - 1]
    else:
        month_num = months.index(month) + 1

    # get the maximum days in the specified month
    if month_num == 2:
        leap_year = isLeapYear(year)
        max_days = month_days[1][leap_year]
    else:
        max_days = month_days[month_num - 1]

    this_week = range(day, day + 7)
    # check if days go past the maximum
    if this_week[6] > max_days:
        num_over = this_week[6] - max_days
        index = 7 - num_over
        # adjust overflow dates to the next month
        for i, value in enumerate(this_week[index:]):
            this_week[index + i] = i + 1
        # get next month's soup
        month2 = months[month_num]
        soup2 = getSoup(month2, year)

    soup = getSoup(month, year)

    shows = "Week of {0} {1}, {2}:\n".format(month, day, year)
    for day in this_week:
        match = re.compile('\s*' + str(day) + '\s*')
        if day >= this_week[0]:
            try:
                day_info = soup.find(class_="caldate", text=match).parent
            except:
                day_info = soup.find(text=match).parent
            day_info = day_info.find_all("p")
            info, dump = parseDay(day_info, month, year, find=find)
            shows += info
        else:
            try:
                day_info = soup2.find(class_="caldate", text=match).parent
            except:
                day_info = soup2.find(text=match).parent
            day_info = day_info.find_all("p")
            info, dump = parseDay(day_info, month2, year, find=find)
            shows += info
            
    return shows

# legacy function originally intended to get the entire month; works properly
# but twilio does not seem to send responses this long. switched to weekly scale
def findInMonth(month, year, find, info=False, timeout=3):
    soup = getSoup(month, year)
    
    results = []
    weeks = soup.find(id="calendar").find_all("tr")
    for week in weeks:
        days = week.find_all("td")    
        for day in days:
            day_info = day.find_all("p")
            dump, results = parseDay(day_info, month, year, find=find,
                                        info=info, results=results)
            
    if not results and timeout > 1:
        next_month = months.index(month) + 1
        next_index = next_month % 12 
        year += next_month / 12 

        return findInMonth(month, year, find, timeout=(timeout - 1))
    else:
        return results


#############################
##        Top-Level        ##
#############################

# basic usage of the service
def makeSpecial():
    s = "List films playing...\n"
    s += "    TODAY\n"
    s += "    WEEK\n"
    s += "    FROM [day] [month] [year, 2007 onwards]\n    "
    s += "  *lists week starting on this date, default current date*\n\n"
    s += "Or search for a film title...\n"
    s += "    FIND (search-term) [starting month] [starting year]\n"
    s += "    INFO (search-term) [starting month] [starting year]\n\n"
    s += "Find the start time of a film, or get info and a description.\n"
    s += "Searches for three months. Starts searching in the current month "
    s += "by default.\n"
    return s

special = makeSpecial()

# parses input in evaluation
def eval(cmd):
    find = False
    info = False
    searches = []

    week_of = False
    month = None
    day = None
    year = None

    for word in cmd:
        if word:
            # get capital word for month info and service commands
            word = word.encode('ASCII')
            capital = word[0].upper() + word[1:].lower()
            month_check = capital.replace(",", "")

            # convert to int for specifying days and years
            try:
                int_val = word.replace(",", "")
                int_val = int(int_val)
            except:
                int_val = 0
        
            # Search for mode arguments
            if capital == "Today":
                return getToday()
            elif capital == "From":
                week_of = True
            elif capital == "Week":
                return getWeek()
            elif capital == "Info":
                find = True
                info = True 
            elif capital == "Find":
                find = True
            # search for date specifiers
            elif month_check in months and not month:
                month = month_check
            elif int_val in max_days and not find:
                day = int_val
            elif int_val in max_years:
                year = int_val
            # add other terms to search, factoring out command tags
            elif capital not in ["Movies", "Movie", "Films", "Film"]:
                searches.append(capital.lower()) 

    if week_of:
        try:
            return getWeek(day=day, month=month, year=year) 
        except:
            return "No data could be found for the specified week.\n"
    elif find:
        # get starting point if not specified
        now = datetime.now()
        if not month:
            month = months[now.month - 1]
        if not year:
            year = now.year

        search = " ".join(searches)
        if not search:
            return "Specify a term to search for."
        else:
            results = findInMonth(month, year, search, info=info) 
            response = ""
            # seach return value depends on if info was also searched for
            for result in results:
                if info:
                    response += '"' + search + '":\n'
                    response += "  " + result[0] + "\n\n"
                    response += result[1]
                else:
                    response += "  " + result + "\n"

            if not response:
                return ("No results found for '{0}' within three months of " +
                    "{1}, {2}.\n").format(search, month, year)
            else:
                if not info:
                    response = "Searching for '" + search + "':\n" + response
                return response 
    else:
        return special
