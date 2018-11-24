import urllib2, urllib
import re
from bs4 import BeautifulSoup
from datetime import date
import calendar

def getYelpData(input) :
    try:
        #construct search url
        url = 'https://www.yelp.com/search?find_desc=' + urllib.quote_plus(input.strip()) + '&find_loc=harvard%20yard'
        hdr = {'User-Agent': 'Chrome'}
        req = urllib2.Request(url,headers=hdr)
        website = urllib2.urlopen(req)
                                
        #construct business url based on search results
        tempurl = "https://www.yelp.com" + re.search("href=\"(/biz.+?)\"", website.read()).group(1)
        hdr = {'User-Agent': 'Chrome'}
        req = urllib2.Request(tempurl,headers=hdr)
        website = urllib2.urlopen(req)

        soup = BeautifulSoup(website.read(), 'html.parser')

        #find business hours
        bizhourstag = soup.find(class_ = "biz-hours")
        bizhours = ""
        try: 
            bizhours = (calendar.day_name[date.today().weekday()] 
            + ": " 
            + bizhourstag.findChildren("span", class_ = "nowrap", recursive=True)[0].string.strip() 
            + " - " 
            + bizhourstag.findChildren("span",class_ = "nowrap", recursive=True)[1].string.strip() 
            + "\n")
        except Exception,e:
            pass

        #find business address
        addresstag = soup.find_all("address")
        address = "" if (not addresstag or not addresstag[1]) else addresstag[1].string.strip() + "\n"

        #find business name
        nametag =   (soup.find("h1", class_ = "biz-page-title embossed-text-white shortenough") 
                    or 
                    soup.find("h1", class_ = "biz-page-title embossed-text-white"))
        name = "" if not nametag else nametag.string.strip() + "\n"

        #find business phone
        phonetag = soup.find_all(class_ = "biz-phone")
        phone = "" if not phonetag else phonetag[0].string.strip() + "\n"

        #construct return value.
        body = (name or "") + (address or "") + (bizhours or "") + (phone or "") + tempurl
        return body
    except Exception, e:
        print(e)
        return "Unable to find business."



special = "Usage: yelp (business name). Provides phone number, yelp url, and today's hours."

def eval(input):
    return getYelpData(input)

print getYelpData("cafe")