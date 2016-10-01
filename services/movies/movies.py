import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

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

def getWeek():
    now = datetime.now()
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
            
    print shows

def makeSpecial():
    s = "To list the movies playing for a particular month use 'movie month'"
    return s

special = makeSpecial()

def eval(cmd):
    return getMovies(cmd)
