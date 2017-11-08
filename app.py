from flask import Flask, request, redirect
import twilio.twiml
import data
from services import *

# import get and Beautiful Soup
from requests import get
from bs4 import BeautifulSoup

app = Flask(__name__)

## the sublist of commands that contain the given tag
def filter(tag,cmds=data.box):
    return [cmd for cmd in cmds if tag in cmd['tags']]

## evaluates a given command to a string by delegating to the proper service
def eval(cmd, input=None):
    s = ""
    if cmd['service'] == 'L': ## Laundry
        return laundry.eval(cmd['args'])
    elif cmd['service'] == 'S': ## Shuttle
        return shuttle.eval(cmd['args'])
    elif cmd['service'] == 'W': ## Weather
        return weather.eval(input)
    else:
        return "ERROR 42: service not recognized"

## list of services that need the user's input to work, not a command
def needsInput(cmd):
    return cmd['service'] in ['W']

def special(incoming):
    body = ''
    if incoming.upper() == "SHUTTLE" :
        body = shuttle.special
    elif incoming.upper() == "LAUNDRY":
        body = laundry.special
    elif incoming.upper() == "WEATHER":
        body = weather.special
    elif incoming.upper() == "DEMO":
        ## welcome/instructions
        body = 'Thanks for using Harvard Now!\n'
        body += 'Laundry Information is accessed by sending the name of your laundry room\n'
        body += 'e.g. Lowell D\n'
        body += 'For a list of all laundry rooms send laundry\n\n'
        body += 'To access shuttle information send the name of the stop or name of the route\n'
        body += 'e.g. Widener Gate; Quad Yard Express\n'
        body += 'For a list of all shuttle stops and routes send shuttle\n\n'
        body += 'Sending part of a name gives all information associated with that name.\n'
        body += 'For example sending Quad will give information about the shuttle stop Quad and the shuttle'
        body += 'route Quad Yard Express and sending Quincy laundry will give all the laundry rooms in Quincy.\n'
    elif incoming.upper() == "MOVIE":
        movies = pullMovieData()
        body += 'Thanks for using harvard now: \n'
        body += 'to get movie information, type: movie [title]\n'
        body += 'if you typed the most popular movie, you would get\n'
        body += "title: { } year:  { } imdb rating:  { }".format(movies[0].title,movies[0].year,movies[0].imdb_rating)
    return body

# Make the movie class
class movie:
    def __init__(self, title, year,imbd_rating,meta_rating,votes):
        self.title = title
        self.year = year
        self.imbd_rating = imbd_rating
        self.meta_rating = meta_rating
        self.votes = votes

# the url for pullimg movies

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

## have a method for pullimg movie data from imdb
def pullMovieData():
    movies = []
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
    # go through the first 50 movies from the page
    if container.find('div',class_ = 'ratings-metascore') is not None:
        # name
        name = container.h3.a.text


        # year
        year = container.h3.find('span',class_ = 'lister-item-year text-muted unbold').text

        # imbd rating
        imdb = float(container.strong.text)

        # metacritic rating
        meta = container.find('span', class_ = 'metascore favorable')

        # votes
        votes = container.find('span', attrs = {'name':'nv'})['data-value']

        newMovie = movie(name,year,imdb,meta,votes)
        movies.append(newMovie)

    return(movies)


## main function
@app.route("/", methods=['GET', 'POST'])
def response():
    resp = twilio.twiml.Response()
    incoming = request.values.get('Body',None)

    ## first check if the query is a special case
    body = special(incoming.replace(' ',''))
    if body != '':
        resp.message(body)
        return str(resp)
    ## if not, continue with command filtering
    words = set(incoming.upper().split(" "))
    started = False
    isMovie = False
    results = data.box
    for word in words:
        r = filter(word,results)
        if r == []:
            continue
        else:
            started = True
            results = r
            # if the word movie was just said
        if isMovie== True:
            movies = pullMovieData()
            for movie in movies:
                if word in movie.title:
                    body = "title: {} year:  {} imdb rating:  {}".format(movie.title, movie.year, movie.imdb_rating)
                    return(str(resp.message(body)))
                    started = True
            if started == False:
                isMovie = False
        if word == "movie":
            isMovie = True


    if not started:
        body = "Sorry, I don't know what that is."
    elif len(results) > 12:
        body = "Sorry, that's too many requests."
    else:
        if any(needsInput(cmd) for cmd in results):
            body = "\n".join(['\n'+eval(cmd, words) for cmd in results])
        else:
            body = "\n".join(['\n'+eval(cmd) for cmd in results])

    resp.message(body)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
