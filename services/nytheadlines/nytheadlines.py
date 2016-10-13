"""
Implements the NYT article finding function
Author: Austin Tripp

credits to: http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial
(their tutorial was quite helpful)
"""
from nytimesarticle import articleAPI

# Load the API from my unique key
api = articleAPI("cbecb14f7e854784bec180e71ef94614")


# Turns the articles dictionary into a single string response
def articles_to_str(articles, start=""):
    resp = start
    for i, a in enumerate(articles['response']['docs']):
        resp += '\n{})'.format(i+1) + a['headline']['main']
    return resp


# NYT Searching function
def nyt_search(term):
    term = term.replace('_', " ")
    articles = api.search(q=term)
    return articles_to_str(articles, start='Search results for "{}":'.format(term))


# NYT General Headlines function
def nyt_headlines():
    articles = api.search()
    return articles_to_str(articles, start="Headlines: ")


# Mandatory functions/things
special = 'Enter "nyt search THING" to search for THING in the New York Times Headlines.' + \
    ' Or, type "nyt headlines" to get the latest headlines from anywhere.' + \
    "\nNote: multiple-word searches must be separated with underscores instead of spaces"
error_str = "Sorry, NYT headlines wasn't sure what that request wanted.\nHint: " + special


def eval(cmd, input):
    # Check if it is searching or not
    if 'SEARCH' in input:

        # Find which search parameters they wanted
        input.remove('SEARCH')
        if 'NYT' in input:
            input.remove('NYT')
        try:
            search_term = input.pop()
            return nyt_search(search_term)
        except KeyError:
            return error_str
    elif 'HEADLINES' in input:
        return nyt_headlines()
    else:
        return error_str
