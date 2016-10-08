#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re

# we'd like to have tags like both Kendall and MIT for station Kendall/MIT
# so we will be splitting the station name on both spaces and /
splitter = re.compile(r"[\s/]+")

# output template for a line in data.py that we will output
template = "{'service': 'MBTA', 'args': {'pg': %s}, 'tags': %s},"

# tags shared by everything dealing with MBTA T Subway stuff
base_tags = ['MBTA', 'SUBWAY', 'T', 'SCHEDULE', 'LINE']

# these are stations that are on multiple lines, they are coded here by
# a subset of their name that distinguishes them from others, but also catches
# all the various forms
stations_with_multiple = {
    'park st': (set(), set()),
    'downtown': (set(), set()),
    'government': (set(), set()),
    'north station': (set(), set()),
    'state': (set(), set()),
    'haymarket': (set(), set())
}

# abbreviations we'd like to accept all version of as tags, for instance
# user should be able to type 'harvard sq' or 'harvard square'
abbreviations = [
    ('SQUARE', 'SQ'),
    ('STREET', 'ST')
]


def splice_in_abbr(tags):
    for group in abbreviations:
        for g in group:
            if g in tags:
                tags.update(group)
                break
    return tags


def has_multiple(station):
    station = station.lower()
    for x in stations_with_multiple:
        if x in station:
            return x
    else:
        return None


def print_template(pg, tags):
    print(template % (
        repr(list(pg)),
        repr(base_tags + list(splice_in_abbr({x.upper() for x in tags})))
    ))


def handle_subway_line(a_tags, line_name):
    # for loop over the <a> tags we have, skipping over the ones that are not
    # station names
    for a in filter(lambda x: not x.get('name'), a_tags):
        # register the stations that live on multiple lines globally, otherwise
        # just work locally
        h = has_multiple(a.string)
        if h is not None:
            pg, tags = stations_with_multiple[h]
        else:
            pg = set()  # set of url parts to the page to scrape
            tags = set()  # set of station-specific tags to catch
        pg.add(a.get('href'))
        tags.add(line_name)
        tags.update(splitter.split(a.string.upper()))

        # render the template locally if this station is on one line only
        if h is None:
            print_template(pg, tags)


def main():
    for n in ('green', 'red', 'orange', 'blue'):
        with open(n + '.txt') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            a_tags = soup.findAll('a')
            handle_subway_line(a_tags, n)

    # render templates for stations that live on multiple lines (after
    # collecting all possibilities)
    for s in stations_with_multiple:
        pg, tags = stations_with_multiple[s]
        print_template(pg, tags)


if __name__ == "__main__":
    main()
