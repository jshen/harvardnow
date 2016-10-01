import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

month_days = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]

def isLeapYear(year):
    if year % 4 != 0:
        return 0
    elif year % 100 != 0:
        return 1
    elif year % 400 == 0:
        return 1
    else:
        return 0

def parseDay(day_info, month, year):
    shows = ""
    try:
        day_title = month + " " + day_info[0].getText()
        showtime = len(day_info[1].getText())
    except:
        showtime = 0
    if showtime > 1:
        datetime_string = day_title + " " + str(year)
        time = datetime.strptime(datetime_string, "%B %d %Y")
        weekday_num = time.weekday()
        weekday = weekdays[weekday_num]
        day_title = weekday + ", " + day_title + ":\n"

        shows += day_title 
        show_info = "  "
        day_shows = day_info[1:]
        for index, show in enumerate(day_shows):
            show_info += show.getText()                
            if show["class"][0] == "calfilm":
                shows += show_info + "\n"
                try:
                    next_el = day_shows[index + 1]
                    if next_el["class"][0] == "calnote":
                        shows += "    *" + next_el.getText() + "\n"
                except:
                    pass
                show_info = "  "
        show_info += "\n"
    return shows

def getSoup(month, year):
    month = month.lower()
    year = str(year)[-2::]
    url = "http://hcl.harvard.edu/hfa/calendar/{0}{1}.html".format(month, year)
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), "lxml")
    return soup

def getWeek():
    now = datetime.now()
    day = now.day
    month_num = now.month
    month = months[month_num - 1]
    year = now.year

    if month_num == 2:
        leap_year = isLeapYear(year)
        max_days = month_days[1][leap_year]
    else:
        max_days = month_days[month_num - 1]

    this_week = range(day, day + 7)
    if this_week[6] > max_days:
        num_over = this_week[6] - max_days
        index = 7 - num_over
        for i, value in enumerate(this_week[index:]):
            this_week[index + i] = i + 1
        month2 = months[month_num]
        soup2 = getSoup(month2, year)

    soup = getSoup(month, year)

    shows = ""
    for day in this_week:
        if day >= this_week[0]:
            day_info = soup.find(text=str(day)).parent.parent
            day_info = day_info.find_all("p")
            shows += parseDay(day_info, month, year)
        else:
            day_info = soup2.find(text=str(day)).parent.parent
            day_info = day_info.find_all("p")
            shows += parseDay(day_info, month2, year)
            
    print shows

def getMonth(cmd):
    month = cmd[0].upper() + cmd[1:]
    year = datetime.now().year
    soup = getSoup(month, year)
    
    shows = ""
    weeks = soup.find(id="calendar").find_all("tr")
    for week in weeks:
        days = week.find_all("td")    
        for day in days:
            day_info = day.find_all("p")
            # ignore empty days
            shows += parseDay(day_info, month, year)
            
    print shows

def makeSpecial():
    s = "To list the movies playing for a particular month use 'movie month'"
    return s

special = makeSpecial()

def eval(cmd):
    return getMovies(cmd)
