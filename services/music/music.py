from bs4 import BeautifulSoup
import urllib2
import data

def getSongs():
  url = "http://www.billboard.com/charts/hot-100"
  website = urllib2.urlopen(url)
  soup = BeautifulSoup(website.read(), 'html.parser')

  songs = soup.findAll("h2", {"class": "chart-row__song"})

  song_1 = songs[0].text
  song_2 = songs[1].text
  song_3 = songs[2].text
  song_4 = songs[3].text
  song_5 = songs[4].text
  song_6 = songs[5].text
  song_7 = songs[6].text
  song_8 = songs[7].text
  song_9 = songs[8].text
  song_10 = songs[9].text
  song_11 = songs[10].text
  song_12 = songs[11].text
  song_13 = songs[12].text
  song_14 = songs[13].text
  song_15 = songs[14].text
  song_16 = songs[15].text
  song_17 = songs[16].text
  song_18 = songs[17].text
  song_19 = songs[18].text
  song_20 = songs[19].text

  artists = soup.findAll("a", {"class": "chart-row__artist"})

  artist_1 = artists[0].text.strip()
  artist_2 = artists[1].text.strip()
  artist_3 = artists[2].text.strip()
  artist_4 = artists[3].text.strip()
  artist_5 = artists[4].text.strip()
  artist_6 = artists[5].text.strip()
  artist_7 = artists[6].text.strip()
  artist_8 = artists[7].text.strip()
  artist_9 = artists[8].text.strip()
  artist_10 = artists[9].text.strip()
  artist_11 = artists[10].text.strip()
  artist_12 = artists[11].text.strip()
  artist_13 = artists[12].text.strip()
  artist_14 = artists[13].text.strip()
  artist_15 = artists[14].text.strip()
  artist_16 = artists[15].text.strip()
  artist_17 = artists[16].text.strip()
  artist_18 = artists[17].text.strip()
  artist_19 = artists[18].text.strip()
  artist_20 = artists[19].text.strip()

  print "1. "+ song_1 + ": " + artist_1
  print "2. "+ song_2 + ": " + artist_2
  print "3. "+ song_3 + ": " + artist_3
  print "4. "+ song_4 + ": " + artist_4
  print "5. "+ song_5 + ": " + artist_5
  print "6. "+ song_6 + ": " + artist_6
  print "7. "+ song_7 + ": " + artist_7
  print "8. "+ song_8 + ": " + artist_8
  print "9. "+ song_9 + ": " + artist_9
  print "10. "+ song_10 + ": " + artist_10
  print "11. "+ song_11 + ": " + artist_11
  print "12. "+ song_12 + ": " + artist_12
  print "13. "+ song_13 + ": " + artist_13
  print "14. "+ song_14 + ": " + artist_14
  print "15. "+ song_15 + ": " + artist_15
  print "16. "+ song_16 + ": " + artist_16
  print "17. "+ song_17 + ": " + artist_17
  print "18. "+ song_18 + ": " + artist_18
  print "19. "+ song_19 + ": " + artist_19
  print "20. "+ song_20 + ": " + artist_20
  
  
def special(incoming):
    body = ''
    if incoming.upper() == "MUSIC" :
        body = music.special
    elif incoming.upper() == "DEMO":
      
        ## welcome/instructions
        body = 'Thanks for using Harvard Now!\n'
        body += 'Text Music to view the Billboard Top 20 songs of the week\n'
    return body
    
def eval(cmd):
    return cmd['label']+'\n'+machines_to_string(getMachines(cmd['roomid'],cmd['machinetype']))
