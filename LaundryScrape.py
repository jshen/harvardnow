import urllib2, urllib
from bs4 import BeautifulSoup

## dictionary of rooms (name : id)
rooms = {
    'CANADAY HALL'                        : "1362584",
    'CURRIER HOUSE - DANIELS HALL'        : "1362585",
    'LOWELL HOUSE N'                      : "1362586",
    'THAYER HALL'                         : "1362588",
    'STOUGHTON HALL'                      : "1362589",
    'KIRKLAND HOUSE J'                    : "1362525",
    '24 PRESCOTT ST'                      : "13625149",
    '20 PRESCOTT ST'                      : "13625150",
    '22 PRESCOTT ST'                      : "13625151",
    '1202 MASS AVE 4TH FLR LR'            : "13625152",
    '1201 MASS AVE 3RD FLR LR'            : "13625153",
    'WELD HALL'                           : "136259",
    'WELD'                                : "136259",
    '8 PLYMPTON STREET'                   : "014711",
    'STONE HALL '                         : "13625933",
    'CURRIER HOUSE - BINGHAM HALL'        : "1362510",
    'CABOT HOUSE - BERTRAM HALL'          : "1362511",
    'CABOT HOUSE - WHITMAN HALL'          : "1362512",
    'PFORZHEIMER HOUSE - COMSTOCK HALL'   : "1362513",
    'PFORZHEIMER HOUSE - MOORS HALL'      : "1362514",
    'GREENOUGH HALL'                      : "1362516",
    'WIGGLESWORTH HALL'                   : "1362518",
    'DUNSTER HOUSE K'                     : "1362520",
    'DUNSTER HOUSE G'                     : "1362521",
    'ELIOT HOUSE J'                       : "1362523",
    'PFORZHEIMER HOUSE - WOLBACH HALL'    : "1362554",
    'LEVERETT HOUSE F TOWER'              : "1362526",
    'LEVERETT HOUSE G TOWER'              : "1362527",
    'LOWELL HOUSE G '                     : "1362528",
    'LOWELL HOUSE D'                      : "1362529",
    'LEVERETT HOUSE MCKINLOCK'            : "1362530",
    'NEW QUINCY-6TH FLOOR'                : "1362531",
    'NEW QUINCY-BASEMENT STUDENT LAUNDRY' : "1362532",
    '1306 MASS AVE'                       : "1362533",
    '65 MOUNT AUBURN STREET'              : "1362534",
    'WINTHROP - STANDISH'                 : "1362535",
    'WINTHROP - GORE'                     : "1362536",
    'CABOT HOUSE - ELLIOT HALL'           : "1362537",
    'PFORZHEIMER HOUSE - JORDAN NORTH'    : "1362539",
    'CABOT HOUSE - BRIGGS HALL'           : "1362540",
    'HURLBUT HALL'                        : "1362541",
    'KIRKLAND HOUSE G'                    : "1362545",
    'ADAMS HOUSE'                         : "1362546",
    'APLEY COURT'                         : "1362547",
    'MATHER HOUSE HIGH-RISE'              : "1362548",
    'PFORZHEIMER HOUSE - HOLMES HALL'     : "1362549",
    'CURRIER HOUSE - GILBERT HALL'        : "1362551",
    'CURRIER HOUSE - TUCHMAN HALL'        : "1362552",
    '10 DEWOLFE STREET'                   : "144633",
    '20 DEWOLFE STREET'                   : "144634",
    'CLAVERLY HALL'                       : "1362555",
    'MATHER HOUSE LOW-RISE'               : "1362556",
    'PFORZHEIMER HOUSE - JORDAN SOUTH'    : "1362557"
}


## for each room, scrape the html describing the machines in that room,
## find the washers and add them as dictionaries to the washers list

def getMachines(room, machinetype):
    room = room.upper()
    if room not in rooms.keys(): return "Invalid room name"
    roomid = rooms[room]
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

def room_names():
    s='Here are the laundry rooms that we have data for: \n'
    used = []
    for room in rooms:
        if rooms[room] not in used:
            s+=room+'\n'
            used.append(rooms[room])
    return s
