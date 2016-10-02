import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def parseDay(day_info, month):
    shows = ""
    try:
        day_title = month + " " + day_info[0].getText() + ":\n"
        showtime = len(day_info[1].getText())
    except:
        showtime = 0
    if showtime > 1:
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

def getToday():
    resp = "Movies playing today:\n"
    now = datetime.now()
    day = now.day
    month = now.month
    month_name = months[month - 1].lower()
    year = str(now.year)[-2::]
    url = "http://hcl.harvard.edu/hfa/calendar/{0}{1}.html".format(month_name, year)
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read())
    day_info = soup.find(text=str(day)).parent.parent
    day_info = day_info.find_all("p")
    resp += parseDay(day_info, month_name)
    return resp


def getWeek(day=None, month=None, year=None):
    now = datetime.now()
    if not day:
        day = now.day
    if not month:
        month = now.month
    if not year:
        year = now.year
    day = now.day
    month = now.month
    year = str(now.year)[-2::]
    url = "http://hcl.harvard.edu/hfa/calendar/{0}{1}.html".format(month, year)
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read())
    print day, month, year
    print soup.find(text=str(day)).parent.parent

def getMonth(cmd):
    cmd = cmd.lower()
    month = cmd[0].upper() + cmd[1:]
    year = str(datetime.now().year)[-2::]
    url = "http://hcl.harvard.edu/hfa/calendar/{0}{1}.html".format(cmd, year)
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read())
    
    shows = ""
    weeks = soup.find(id="calendar").find_all("tr")
    for week in weeks:
        days = week.find_all("td")    
        for day in days:
            day_info = day.find_all("p")
            # ignore empty days
            shows += parseDay(day_info, month)
            
    return shows

def makeSpecial():
    s = "List movies playing...\n"
    s += "  Today\n"
    s += "  Week (this week)\n"
    s += "  From [day] [month] [year, 2007 onwards]\n"
    s += "    (the week starting on this date, default today)\n\n"
    s += "Or search for a movie title."
    return s

special = makeSpecial()

max_days = range(1, 32)
max_years = range(2007, datetime.now().year)
def eval(cmd):
    month = ""
    # add get week from function
    
    week_of = False
    month = None
    day = None
    year = None
    for word in cmd:
        if word:
            print word
            word = word.encode('ASCII')
            capital = word[0].upper() + word[1:].lower()
            try:
                int_val = int(word)
            except:
                int_val = 0
        
            if capital == "Today":
                return getToday()
            if capital == "From":
                week_of = True
            elif capital in months:
                month = word 
            elif int_val in max_days:
                day = word
                #getMonth(capital)
            elif int_val in max_years:
                year = word

    if week_of:
        if not day:
            day = datetime.now().day
        if not year:
            year = datetime.now().year
        if not month:
            month = months[datetime.now().month - 1]

        return str(day) + " " + month + " " + str(year)
    else:
        return special
