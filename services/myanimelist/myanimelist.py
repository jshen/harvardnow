# sorry I'm using Python 3 :')
try:
	import urllib.request as urllib2
except ImportError:
	import urllib2
import re
from bs4 import BeautifulSoup

def getMALData(input):
	parse = re.compile('(?:(\d+ latest)|(top \d+ all)|(top \d+ airing)|(.+))$')
	match = parse.match(input)
	body = ""
	# myanimelist/mal heading
	# if followed by "number latest"
	if match.group(1) != None:
		num = int(match.group(1)[:-7])
		body = "Latest " + str(num) + " episodes:\n"
		if (num > 10):
			return "Too many anime"
		elif (num < 0):
			return "Too little anime"
		try:
			url = 'http://myanimelist.net/watch/episode'
			latest = urllib2.urlopen(url)
			soup = BeautifulSoup(latest.read(), 'html.parser')

			animeList = soup.find(id='content').find_all(class_='video-list-outer-vertical')[:num]
			for anime in animeList:
				title = anime.find(class_='mr4').text
				episode = anime.find('a').text
				body += title + ": " + episode + "\n"
		except Exception as e:
			print(str(e))
			return "Could not process query"

	# if followed by "top number all"
	elif match.group(2) != None:
		num = int(match.group(2)[4:-4])
		body = "Top " + str(num) + " Overall Anime\n"
		if (num > 10):
			return "Too many anime"
		elif (num < 0):
			return "Too little anime"
		try:
			url = 'https://myanimelist.net/topanime.php'
			top_all = urllib2.urlopen(url)
			soup = BeautifulSoup(top_all.read(), 'html.parser')

			animeList = soup.find(id='content').find(class_='pb12').find_all(class_='ranking-list')[:num]
			for anime in animeList:
				title = anime.find(class_='di-ib').find('a').text
				info = anime.find(class_='information di-ib mt4').text.strip().split('\n')[0]
				score = anime.find(class_='score').find(class_='text').text + "/10"
				body += title + ": " + info + ", " + score + "\n"
		except Exception as e:
			print(str(e))
			return "Could not process query"

	# if followed by "top number airing"
	elif match.group(3) != None:
		num = int(match.group(3)[4:-7])
		body = "Top " + str(num) + " Airing Anime\n"
		if (num > 10):
			return "Too many anime"
		elif (num < 0):
			return "Too little anime"
		try:
			url = 'https://myanimelist.net/topanime.php?type=airing'
			top_airing = urllib2.urlopen(url)
			soup = BeautifulSoup(top_airing.read(), 'html.parser')

			animeList = soup.find(id='content').find(class_='pb12').find_all(class_='ranking-list')[:num]
			for anime in animeList:
				title = anime.find(class_='di-ib').find('a').text
				info = anime.find(class_='information di-ib mt4').text.strip().split('\n')[0]
				score = anime.find(class_='score').find(class_='text').text + "/10"
				body += title + ": " + info + ", " + score + "\n"
		except Exception as e:
			print(str(e))
			return "Could not process query"
	# if none of these, take the rest and search mal with it
	# return the top 3 results: name, type (eps), score
	else:
		query = input
		incl_link = False
		if len(query) > 50:
			return "Query too long"
		if query.strip().startswith('-l'):
			incl_link = True
			query = query[3:].strip()
		body = "Results for " + query + ":\n"
		try:
			url = 'https://myanimelist.net/search/all?q=' + query
			search = urllib2.urlopen(url)
			soup = BeautifulSoup(search.read(), 'html.parser')

			animeList = soup.find('article').find_all(class_='list di-t w100')[:3]
			for anime in animeList:
				title_html = anime.find(class_='information').find('a')
				title = title_html.text
				info_html = anime.find(class_='fn-grey4')
				info_box = [info for info in info_html.text.split('\n') if info != '']
				info = info_box[0].strip()
				score = info_box[1].strip()[-4:] + "/10"
				# if it includes -l, link to w/e
				body += title + ": " + info + ", " + score + (", " + title_html['href'] if incl_link else '') + "\n"
		except Exception as e:
			print(str(e))
			return "Could not process query"

	return body

print(getMALData('-l kobayashi'))

def makeSpecial():
	s = 'To get information from MAL, start a command with myanimelist or mal\n'
	s += 'To get the latest released anime, use the format \'number latest\'.'
	s += 'Similarly, to get overall top anime, use \'top number all\', and '
	s += 'to get the top currently airing anime, use \'top numbe rairing\'.\n'
	s += 'To search, use \'mal/myanimelist query\'. If you want to include links, use \'mal/myanimelist -l query\'.'
	return s

special = makeSpecial()

def eval(input):
	return getMALData(input)

