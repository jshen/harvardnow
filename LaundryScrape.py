import urllib2, urllib
from bs4 import BeautifulSoup

washers = []

url = "http://m.laundryview.com/submitFunctions.php?cell=null&lr=136259&monitor=true"
website = urllib2.urlopen(url)
soup = BeautifulSoup(website.read(),'html.parser')
washer_div = soup.find(id="washer")
washer = washer_div.next_sibling
while ('id' not in washer.attrs) or washer['id'] != "dryer":
    print washer
    washers.append({
        'lr':'136259', ## LR number for Weld
        'id':washer.a['id'],
        'name':`washer.a.text`.split('\\xa0')[0][2:],
        'time':washer.a.p.text
    })
    washer = washer.next_sibling

for washer in washers:
    print washer
    
