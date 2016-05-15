import urllib2, urllib
from bs4 import BeautifulSoup
import data

#############################
##    Laundry Function     ##
#############################    

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
    for room in data.rooms:
        if data.rooms[room] not in used:
            s += room + '\n'
            used.append(data.rooms[room])
    return s

def makeSpecial():
    s = "Laundry Rooms: \n"
    s += '\n'.join([room for room in data.rooms])
    return s
    
############################
##       Top-Level        ##
############################

## return list of valid laundry rooms
special = makeSpecial()

def eval(cmd):
    return cmd['label']+'\n'+machines_to_string(getMachines(cmd['roomid'],cmd['machinetype']))
