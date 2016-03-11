import urllib2, urllib
from bs4 import BeautifulSoup

rooms = {
    '10 DEWOLFE STREET'                   : "144633",
    '1201 MASS AVE 3RD FLR LR'            : "1362515",
    '1202 MASS AVE 4TH FLR LR'            : "1362515",
    '1306 MASS AVE'                       : "1362533",
    '20 DEWOLFE STREET'                   : "144634",
    '20 PRESCOTT ST'                      : "1362515",
    '22 PRESCOTT ST'                      : "1362515",
    '24 PRESCOTT ST'                      : "1362514",
    '65 MOUNT AUBURN STREET'              : "1362534",
    '8 PLYMPTON STREET'                   : "014711",
    'ADAMS HOUSE'                         : "1362546",
    'APLEY COURT'                         : "1362547",
    'CABOT HOUSE - BERTRAM HALL'          : "1362511",
    'CABOT HOUSE - BRIGGS HALL'           : "1362540",
    'CABOT HOUSE - ELLIOT HALL'           : "1362537",
    'CABOT HOUSE - WHITMAN HALL'          : "1362512",
    'CANADAY HALL'                        : "1362584",
    'CLAVERLY HALL'                       : "1362555",
    'CURRIER HOUSE - BINGHAM HALL'        : "1362510",
    'CURRIER HOUSE - DANIELS HALL'        : "1362585",
    'CURRIER HOUSE - GILBERT HALL'        : "1362551",
    'CURRIER HOUSE - TUCHMAN HALL'        : "1362552",
    'DUNSTER HOUSE G'                            : "1362521",
    'DUNSTER HOUSE K'                            : "1362520",
    'ELIOT HOUSE J'                       : "1362523",
    'GREENOUGH HALL'                      : "1362516",
    'HURLBUT HALL'                        : "1362541",
    'KIRKLAND HOUSE G'                    : "1362545",
    'KIRKLAND HOUSE J'                    : "1362525",
    'LEVERETT HOUSE F TOWER'              : "1362526",
    'LEVERETT HOUSE G TOWER'              : "1362527",
    'LEVERETT HOUSE MCKINLOCK'            : "1362530",
    'LOWELL HOUSE D'                      : "1362529",
    'LOWELL HOUSE G '                     : "1362528",
    'LOWELL HOUSE N'                      : "1362586",
    'MATHER HOUSE HIGH RISE'              : "1362548",
    'MATHER HOUSE LOW RISE'               : "1362556",
    'NEW QUINCY 6TH FLOOR'                : "1362531",
    'NEW QUINCY BASEMENT STUDENT LAUNDRY' : "1362532",
    'PFORZHEIMER HOUSE - COMSTOCK HALL'   : "1362513",
    'PFORZHEIMER HOUSE - HOLMES HALL'     : "1362549",
    'PFORZHEIMER HOUSE - JORDAN NORTH'    : "1362539",
    'PFORZHEIMER HOUSE - JORDAN SOUTH'    : "1362557",
    'PFORZHEIMER HOUSE - MOORS HALL'      : "1362514",
    'PFORZHEIMER HOUSE - WOLBACH HALL'    : "1362554",
    'STONE HALL '                         : "1362593",
    'STOUGHTON HALL'                      : "1362589",
    'THAYER HALL'                         : "1362588",
    'WELD HALL'                           : "136259",
    'WIGGLESWORTH HALL'                   : "1362518",
    'WIGG'                                : "1362518",
    'WINTHROP - GORE'                     : "1362536",
    'WINTHROP - STANDISH'                 : "1362535"
}
    
def getMachines(roomid, machinetype):
    machines = []
    url = 'http://m.laundryview.com/submitFunctions.php?'
    url += 'cell=null&lr=%s&monitor=true' % roomid
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    washer_div = soup.find(id=machinetype)
    machine = washer_div.next_sibling
    if machinetype == 'washer':
        while 'id' not in machine.attrs or machine['id'] != 'dryer':
            machines.append({'lr': roomid,
             'id': machine.a['id'],
             'name': `(machine.a.text)`.split('\\xa0')[0][2:],
             'time': machine.a.p.text})
            machine = machine.next_sibling
    else:
        while machine and machine.name == 'li':
            machines.append({'lr': roomid,
             'id': machine.a['id'],
             'name': `(machine.a.text)`.split('\\xa0')[0][2:],
             'time': machine.a.p.text})
            machine = machine.next_sibling
    return machines

def machines_to_string(machines):
    s = ''
    for machine in machines:
        s += machine['name'] + ': ' + machine['time'] + '\n'
    return s

def room_names():
    s = 'Here are the laundry rooms that we have data for: \n'
    used = []
    for room in rooms:
        if rooms[room] not in used:
            s += room + '\n'
            used.append(rooms[room])
    return s