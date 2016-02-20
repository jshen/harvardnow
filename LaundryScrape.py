import urllib2, urllib
from bs4 import BeautifulSoup

## dictionary of rooms (id : name)
rooms = {
    "1362584"  : 'CANADAY HALL',
    "1362585"  : 'CURRIER HOUSE - DANIELS HALL',
    "1362586"  : 'LOWELL HOUSE N',
    "1362588"  : 'THAYER HALL',
    "1362589"  : 'STOUGHTON HALL',
    "1362525"  : 'KIRKLAND HOUSE J',
    "13625149" : '24 PRESCOTT ST',
    "13625150" : '20 PRESCOTT ST',
    "13625151" : '22 PRESCOTT ST',
    "13625152" : '1202 MASS AVE 4TH FLR LR',
    "13625153" : '1201 MASS AVE 3RD FLR LR',
    "136259"   : 'WELD HALL',
    "014711"   : '8 PLYMPTON STREET',
    "13625933" : 'STONE HALL ',
    "1362510"  : 'CURRIER HOUSE - BINGHAM HALL',
    "1362511"  : 'CABOT HOUSE - BERTRAM HALL',
    "1362512"  : 'CABOT HOUSE - WHITMAN HALL',
    "1362513"  : 'PFORZHEIMER HOUSE - COMSTOCK HALL',
    "1362514"  : 'PFORZHEIMER HOUSE - MOORS HALL',
    "1362516"  : 'GREENOUGH HALL',
    "1362518"  : 'WIGGLESWORTH HALL',
    "1362520"  : 'DUNSTER HOUSE K',
    "1362521"  : 'DUNSTER HOUSE G',
    "1362523"  : 'ELIOT HOUSE J',
    "1362554"  : 'PFORZHEIMER HOUSE - WOLBACH HALL',
    "1362526"  : 'LEVERETT HOUSE F TOWER',
    "1362527"  : 'LEVERETT HOUSE G TOWER',
    "1362528"  : 'LOWELL HOUSE G ',
    "1362529"  : 'LOWELL HOUSE D',
    "1362530"  : 'LEVERETT HOUSE MCKINLOCK',
    "1362531"  : 'NEW QUINCY-6TH FLOOR',
    "1362532"  : 'NEW QUINCY-BASEMENT STUDENT LAUNDRY',
    "1362533"  : '1306 MASS AVE',
    "1362534"  : '65 MOUNT AUBURN STREET',
    "1362535"  : 'WINTHROP - STANDISH',
    "1362536"  : 'WINTHROP - GORE',
    "1362537"  : 'CABOT HOUSE - ELLIOT HALL',
    "1362539"  : 'PFORZHEIMER HOUSE - JORDAN NORTH',
    "1362540"  : 'CABOT HOUSE - BRIGGS HALL',
    "1362541"  : 'HURLBUT HALL',
    "1362545"  : 'KIRKLAND HOUSE G',
    "1362546"  : 'ADAMS HOUSE',
    "1362547"  : 'APLEY COURT',
    "1362548"  : 'MATHER HOUSE HIGH-RISE',
    "1362549"  : 'PFORZHEIMER HOUSE - HOLMES HALL',
    "1362551"  : 'CURRIER HOUSE - GILBERT HALL',
    "1362552"  : 'CURRIER HOUSE - TUCHMAN HALL',
    "144633"   : '10 DEWOLFE STREET',
    "144634"   : '20 DEWOLFE STREET',
    "1362555"  : 'CLAVERLY HALL',
    "1362556"  : 'MATHER HOUSE LOW-RISE',
    "1362557"  : 'PFORZHEIMER HOUSE - JORDAN SOUTH'
}

## for each room, scrape the html describing the machines in that room,
## find the washers and add them as dictionaries to the washers list

def getMachines(room, machinetype):
    if not (machinetype == "washer" or machingtype == "dryer"):
        return "Invalid machine name"

    roomid = rooms.keys()[rooms.values().index(room)]
    machines = []

    url = "http://m.laundryview.com/submitFunctions.php?"
    url += "cell=null&lr=%s&monitor=true"%roomid
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(),'html.parser')
    washer_div = soup.find(id=machinetype)
    machine = washer_div.next_sibling
    if machinetype == "washer" :
        while ('id' not in machine.attrs) or machine['id'] != "dryer":
            machines.append({
                'lr':roomid,
                'id':machine.a['id'],
                'name':`machine.a.text`.split('\\xa0')[0][2:],
                'time':machine.a.p.text
            })
            machine = machine.next_sibling
    else :
        while (machine and machine.name == 'li'):
            machines.append({
                'lr':roomid,
                'id':machine.a['id'],
                'name':`machine.a.text`.split('\\xa0')[0][2:],
                'time':machine.a.p.text
            })
            machine = machine.next_sibling
    return machines

def machines_to_string(machines):
    s=''
    for machine in machines:
        s+= machine['name']+': '+machine['time']+'\n'
    return s

