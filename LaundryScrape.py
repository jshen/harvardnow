import urllib2, urllib
from bs4 import BeautifulSoup

rooms = {
    "1362584": u'CANADAY HALL',
    "1362585": u'CURRIER HOUSE - DANIELS HALL',
    "1362586": u'LOWELL HOUSE N',
    "1362588": u'THAYER HALL',
    "1362589": u'STOUGHTON HALL',
    "1362525": u'KIRKLAND HOUSE J',
    "13625149": u'24 PRESCOTT ST',
    "13625150": u'20 PRESCOTT ST',
    "13625151": u'22 PRESCOTT ST',
    "13625152": u'1202 MASS AVE 4TH FLR LR',
    "13625153": u'1201 MASS AVE 3RD FLR LR',
    "136259": u'WELD HALL',
    "014711": u'8 PLYMPTON STREET',
    "13625933": u'STONE HALL ',
    "1362510": u'CURRIER HOUSE - BINGHAM HALL',
    "1362511": u'CABOT HOUSE - BERTRAM HALL',
    "1362512": u'CABOT HOUSE - WHITMAN HALL',
    "1362513": u'PFORZHEIMER HOUSE - COMSTOCK HALL',
    "1362514": u'PFORZHEIMER HOUSE - MOORS HALL',
    "1362516": u'GREENOUGH HALL',
    "1362518": u'WIGGLESWORTH HALL',
    "1362520": u'DUNSTER HOUSE K',
    "1362521": u'DUNSTER HOUSE G',
    "1362523": u'ELIOT HOUSE J',
    "1362554": u'PFORZHEIMER HOUSE - WOLBACH HALL',
    "1362526": u'LEVERETT HOUSE F TOWER',
    "1362527": u'LEVERETT HOUSE G TOWER',
    "1362528": u'LOWELL HOUSE G ',
    "1362529": u'LOWELL HOUSE D',
    "1362530": u'LEVERETT HOUSE MCKINLOCK',
    "1362531": u'NEW QUINCY-6TH FLOOR',
    "1362532": u'NEW QUINCY-BASEMENT STUDENT LAUNDRY',
    "1362533": u'1306 MASS AVE',
    "1362534": u'65 MOUNT AUBURN STREET',
    "1362535": u'WINTHROP - STANDISH',
    "1362536": u'WINTHROP - GORE',
    "1362537": u'CABOT HOUSE - ELLIOT HALL',
    "1362539": u'PFORZHEIMER HOUSE - JORDAN NORTH',
    "1362540": u'CABOT HOUSE - BRIGGS HALL',
    "1362541": u'HURLBUT HALL',
    "1362545": u'KIRKLAND HOUSE G',
    "1362546": u'ADAMS HOUSE',
    "1362547": u'APLEY COURT',
    "1362548": u'MATHER HOUSE HIGH-RISE',
    "1362549": u'PFORZHEIMER HOUSE - HOLMES HALL',
    "1362551": u'CURRIER HOUSE - GILBERT HALL',
    "1362552": u'CURRIER HOUSE - TUCHMAN HALL',
    "144633": u'10 DEWOLFE STREET',
    "144634": u'20 DEWOLFE STREET',
    "1362555": u'CLAVERLY HALL',
    "1362556": u'MATHER HOUSE LOW-RISE',
    "1362557": u'PFORZHEIMER HOUSE - JORDAN SOUTH'
}

washers = []
for roomid in rooms.keys():
    url = "http://m.laundryview.com/submitFunctions.php?cell=null&lr=%s&monitor=true"%roomid
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(),'html.parser')
    washer_div = soup.find(id="washer")
    washer = washer_div.next_sibling
    while ('id' not in washer.attrs) or washer['id'] != "dryer":
        washers.append({
            'lr':roomid,
            'id':washer.a['id'],
            'name':`washer.a.text`.split('\\xa0')[0][2:],
            'time':washer.a.p.text
        })
        washer = washer.next_sibling
for washer in washers:
    print washer
    
