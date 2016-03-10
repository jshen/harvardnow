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
    'ADAMS'                               : "1362546",
    'APLEY COURT'                         : "1362547",
    'APLEY'                               : "1362547",
    'CABOT'                               : "MULTIPLE|CABOT|BERTRAM HALL|BRIGGS HALL|ELLIOT HALL|WHITMAN HALL",
    'CABOT HOUSE - BERTRAM HALL'          : "1362511",
    'BERTRAM'                             : "1362511",
    'CABOT HOUSE - BRIGGS HALL'           : "1362540",
    'BRIGGS'                              : "1362540",
    'CABOT HOUSE - ELLIOT HALL'           : "1362537",
    'ELLIOT'                              : "1362537",
    'CABOT HOUSE - WHITMAN HALL'          : "1362512",
    'WHITMAN'                             : "1362512",
    'CANADAY HALL'                        : "1362584",
    'CANADAY'                             : "1362584",
    'CLAVERLY HALL'                       : "1362555",
    'CLAVERLY'                            : "1362555",
    'CURRIER'                             : "MULTIPLE|CURRIER|BINGHAM HALL|DANIELS HALL|GILBERT HALL|TUCHMAN HALL",
    'CURRIER HOUSE - BINGHAM HALL'        : "1362510",
    'BINGHAM'                             : "1362510",
    'CURRIER HOUSE - DANIELS HALL'        : "1362585",
    'DANIELS'                             : "1362585",
    'CURRIER HOUSE - GILBERT HALL'        : "1362551",
    'GILBERT'                             : "1362551",
    'CURRIER HOUSE - TUCHMAN HALL'        : "1362552",
    'TUCHMAN'                             : "1362552",
    'DUNSTER'                             : "MULTIPLE|DUNSTER|DUNSTERG|DUNSTERK",
    'DUNSTERG'                            : "1362521",
    'DUNSTERK'                            : "1362520",
    'ELIOT HOUSE J'                       : "1362523",
    'ELIOT'                               : "1362523",
    'GREENOUGH HALL'                      : "1362516",
    'GREENOUGH'                           : "1362516",
    'HURLBUT HALL'                        : "1362541",
    'HURLBUT'                             : "1362541",
    'KIRKLAND'                            : "MULTIPLE|KIRKLAND|KIRKLANDG|KIRKLANDJ",
    'KIRKLAND HOUSE G'                    : "1362545",
    'KIRKLANDG'                           : "1362545",
    'KIRKLAND HOUSE J'                    : "1362525",
    'KIRKLANDJ'                           : "1362525",
    'LEVERETT'                            : "MULTIPLE|LEVERETT|LEVERETTF|LEVERETTG|MCKINLOCK",
    'LEVERETT HOUSE F TOWER'              : "1362526",
    'LEVERETTF '                          : "1362526",
    'LEVERETT HOUSE G TOWER'              : "1362527",
    'LEVERETTG'                           : "1362527",
    'LEVERETT HOUSE MCKINLOCK'            : "1362530",
    'MCKINLOCK'                           : "1362530",
    'LOWELL'                              : "MULTIPLE|LOWELL|LOWELLD|LOWELLG|LOWELLN",
    'LOWELL HOUSE D'                      : "1362529",
    'LOWELLD'                             : "1362529",
    'LOWELL HOUSE G '                     : "1362528",
    'LOWELLG '                            : "1362528",
    'LOWELL HOUSE N'                      : "1362586",
    'LOWELLN'                             : "1362586",
    'MATHER'                              : "MULTIPLE|MATHER|HIGH-RISE|LOW-RISE",
    'MATHER HOUSE HIGH-RISE'              : "1362548",
    'HIGH-RISE'                           : "1362548",
    'HIGH'                                : "1362548",
    'MATHER HOUSE LOW-RISE'               : "1362556",
    'LOW-RISE'                            : "1362556",
    'LOW'                                 : "1362556",
    'QUINCY'                              : "MULTIPLE|QUINCY|QUINCY-6TH FLOOR|QUINCY-BASEMENT",
    'NEW QUINCY-6TH FLOOR'                : "1362531",
    'QUINCY-6TH'                          : "1362531",
    '6TH'                                 : "1362531",
    'NEW QUINCY-BASEMENT STUDENT LAUNDRY' : "1362532",
    'QUINCY-BASEMENT'                     : "1362532",
    'BASEMENT'                            : "1362532",
    'PFORZHEIMER'                         : "MULTIPLE|PFORZHEIMER|COMSTOCK|HOLMES|JORDAN-NORTH|JORDAN-SOUTH|MOORS|WOLBACH",
    'PFOHO'                               : "MULTIPLE|PFOHO|COMSTOCK|HOLMES|JORDAN-NORTH|JORDAN-SOUTH|MOORS|WOLBACH",
    'PFORZHEIMER HOUSE - COMSTOCK HALL'   : "1362513",
    'COMSTOCK'                            : "1362513",
    'PFORZHEIMER HOUSE - HOLMES HALL'     : "1362549",
    'HOLMES'                              : "1362549",
    'PFORZHEIMER HOUSE - JORDAN NORTH'    : "1362539",
    'JORDAN-NORTH'                        : "1362539",
    'JORDAN-N'                            : "1362539",
    'JORDANN'                             : "1362539",
    'PFORZHEIMER HOUSE - JORDAN SOUTH'    : "1362557",
    'JORDAN-SOUTH'                        : "1362557",
    'JORDAN-S'                            : "1362557",
    'JORDANS'                             : "1362557",
    'PFORZHEIMER HOUSE - MOORS HALL'      : "1362514",
    'MOORS'                               : "1362514",
    'PFORZHEIMER HOUSE - WOLBACH HALL'    : "1362554",
    'WOLBACH'                             : "1362554",
    'STONE HALL '                         : "1362593",
    'STOUGHTON HALL'                      : "1362589",
    'THAYER HALL'                         : "1362588",
    'WELD HALL'                           : "136259",
    'WELD'                                : "136259",
    'WIGGLESWORTH HALL'                   : "1362518",
    'WIGGLESWORTH'                        : "1362518",
    'WIGG'                                : "1362518",
    'WINTHROP'                            : "MULTIPLE|WINTHROP|GORE|STANDISH",
    'WINTHROP - GORE'                     : "1362536",
    'GORE'                                : "1362536",
    'WINTHROP - STANDISH'                 : "1362535",
    'STANDISH'                            : "1362535"
}
    

def getMachines(room, machinetype):
    room = room.upper()
    if room not in rooms.keys():
        return 'Invalid room name'
    roomid = rooms[room]
    if roomid.split('|')[0] == 'MULTIPLE':
        return roomid
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
