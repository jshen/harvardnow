# -*- coding: utf-8 -*-

#import libraries
import urllib2
from bs4 import BeautifulSoup


def getHours(htype):
 
    #specify the URL
    url = 'http://library.harvard.edu/all-library-hours'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page.read(), 'html.parser')
    
    if not((htype == "GH") or (htype == "MH") or (htype == "RH") or (htype == "WPH") or (htype == "WPHS")):
        final_hours = ""
    
    # start search here 
    lamtable = soup.find('table', attrs={'class': 'harvard-library-hours-node-widget', 'data-nid':'246'}).find('tbody').find_all('tr')

    # find correct hours
    if htype == "GH":
        final_hours = lamtable[0].text 
    elif htype == "MH":
        final_hours = lamtable[1].text
    elif htype == "RH":
        final_hours = lamtable[2].text
    elif htype == "WPH":
        final_hours = lamtable[3].text
    elif htype == "WPHS":
        final_hours = lamtable[4].text

    # reutrn hours
    if final_hours == "":
        errorstring = "please enter valid command"
        return errorstring
    else:
        return final_hours


def makeSpecial():
    s = "Get lamont library hours. \n"
    s+= "Select from: \n"
    s+= "General Hours (GH), Media Help (MH), Research Help (RH), Woodberry Poetry Room (WPH), Woodberry Poetry Room Staff (WPHS)"
    return s

#############################
##        Top-Level        ##
#############################

## list of valid shuttles
special = makeSpecial()
def eval(cmd):
    return getHours(cmd['htype']) 
