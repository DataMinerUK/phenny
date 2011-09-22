"""
            newssearch.py - Phenny Newssearch Module
            Copyright 2011, Nicola Hughes
            Licensed under the Eiffel Forum License 2.
            
"""

import urllib2
from xml.dom.minidom import parseString

def gn(phenny, input):
	""".gn Returns the headline and link from Google News for a given search term for a given number """
	QUERY = input.group(2).split(':')[0]
	Number = int(input.group(2).split(':')[1].strip(' '))
	obj = parseString( urllib2.urlopen('http://news.google.com/news?q=%s&output=rss' % QUERY).read() )
	elements = obj.getElementsByTagName('title')[2:] # To get rid of unwanted title elements in XML doc
	links = obj.getElementsByTagName('link')[2:]
	for element in elements[:Number]:
		headline =  element.childNodes[0].data
		for link in links:
			url = link.childNodes[0].data.split('=')[-1]
		newssearch = headline + ' -> ' + url
		phenny.say(newssearch)
    
gn.commands = ['gn']
gn.priority = 'high'
gn.example = '.gn searchterm: number i.e. Syria: 3'
