#!/usr/bin/env /usr/local/bin/python

from bs4 import BeautifulSoup
import urllib2
import sys

url = sys.stdin.readline().strip()

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

page = opener.open(url).read()
soup = BeautifulSoup(page, "html.parser")

sys.stdout.write('"' + soup.title.text + '"')