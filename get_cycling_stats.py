# ProCyclingStats.com scraper
# author: Sky McKinley
# modified: 2/8/2015

import urllib2
import re

def __main__(url, id, *args):
	response = urllib2.urlopen(url)
	page_source = response.read()
	riders = re.findall(r'<a class="BlackToRed" href="rider/(.*?)">', page_source)

	f = open('riderstatsDubaiTour2015.csv', 'w')
	f.write('name, weight, height\n')


	for rider in riders:
		url = 'http://www.procyclingstats.com/rider/' + rider
		response = urllib2.urlopen(url)
		page_source = response.read()
		print(rider)
		weight = re.findall(r'<b>Weight:</b> (\S*?) kg &nbsp; <span>', page_source)
		height = re.findall(r'<b>Height:</b> (\S*?) m<br />', page_source)
		if(weight != [] and height != []):
			f.write(rider + ',' + weight[0] + ',' + height[0] + '\n')
			print(rider + ',' + weight[0] + ',' + height[0])

if __name__ == '__main__':
#	url = 'http://www.procyclingstats.com/race/Santos_Tour_Down_Under_2015-startlist'
#	url = 'http://www.procyclingstats.com/race/Tour_de_San_Luis_2015-startlist'
	url = 'http://www.procyclingstats.com/race.php?id=151112&c=3'
	id = 'href=\"rider'
	__main__(url, id)
