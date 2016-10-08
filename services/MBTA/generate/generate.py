#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re

splitter = re.compile(r"[\s+/]")
template = "{'service': 'MBTA', 'args': {'pg': %s}, 'tags': %s},"
base_tags = ['MBTA', 'SUBWAY', 'T', 'SCHEDULE', 'LINE']

stations_with_multiple = {
    'park st': (set(), set()),
    'downtown': (set(), set()),
    'government': (set(), set()),
    'north station': (set(), set()),
    'state': (set(), set()),
    'haymarket': (set(), set())
}

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
    for a in filter(lambda x: not x.get('name'), a_tags):
        h = has_multiple(a.string)
        if h is not None:
            pg, tags = stations_with_multiple[h]
        else:
            pg = set()
            tags = set()
        pg.add(a.get('href'))
        tags.add(line_name)
        tags.update(splitter.split(a.string.upper()))
        print_template(pg, tags)


def main():
    for n in ('green', 'red', 'orange', 'blue'):
        with open(n + '.txt') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            a_tags = soup.findAll('a')
            handle_subway_line(a_tags, n)

    for s in stations_with_multiple:
        pg, tags = stations_with_multiple[s]
        print_template(pg, tags)


if __name__ == "__main__":
    main()
