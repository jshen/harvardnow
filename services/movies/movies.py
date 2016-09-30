import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

def getMovies(cmd):
    month = cmd.lower()
    year = str(datetime.now().year)[-2::]
    url = "http://hcl.harvard.edu/hfa/calendar/{0}{1}.html".format(month, year)
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')

    shows = ""
    weeks = soup.find(id="calendar").find_all("tr")
    for week in weeks:
        days = week.find_all("td")    
        for day in days:
            day_info = day.find_all("p")
            # ignore empty days
            if len(day_info) > 2:
                shows += cmd + " " + day_info[0].getText() + ":\n"
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
            
    print shows

def makeSpecial():
    s = "To list the movies playing for a particular month use 'movie month'"
    return s

special = makeSpecial()

def eval(cmd):
    return getMovies(cmd)
