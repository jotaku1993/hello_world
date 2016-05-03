import os, shutil
from bs4 import BeautifulSoup
import re
import urllib2

direcInput='/Users/jotaku/Downloads/bigdata/famous/'
direcOutput='/Users/jotaku/Downloads/bigdata/reviews/'

#go through all the famous places
def getUrl(filename):
	f = open(direcInput+filename, 'r')
	lst = f.readlines()
	visited = {}
	for catag in lst:
		if catag not in visited:
			visited[catag] = None
			print add(catag, filename)
	print len(visited)
	f.close()
	return "finished"

#write down the reviews for every link
def add(url, filename):
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser').find('section', id='map-content-view')
	ratings = soup.findAll(attrs={"itemprop":"ratingValue"})
	reviews = soup.findAll(attrs={"class":"review-text"})
	
	#print reviews
	#print '###########'
	openPath = direcOutput + filename[:-5] + '/' + changeSlash(url[25:])
	f= open(openPath,'w')

	if len(ratings) == 0:
		f.write('No ratings')
		f.write('\r\n')
	else:
		f.write(str(ratings[0]))
		f.write('\r\n')

	for review in reviews:
		f.write(str(review))
		f.write('\r\n')

	f.close()
	return 'finished'

#build the dir for the reviews
def makeDir(dire):
	newPath = direcOutput + dire
	if not os.path.isdir(newPath):
		os.makedirs(newPath)

#delete the slash in the filename
def changeSlash(s):
	ret = ''
	for i in range(len(s)):
		if s[i] != '/':
			ret += s[i]
		else:
			ret += '-'
	ret += '.txt'
	return ret

if __name__ == '__main__':
	#add('https://roadtrippers.com/us/orlando-fl/attractions/universal-studios-orlando', 'test.txt')
	
	i = 0
	for famous in os.listdir(direcInput):
		######
		if i >= 1:
			break
		######
		if famous.endswith('txt'):
			print i
			i+=1
			print famous[:-5]
			makeDir(famous[:-5])
			print getUrl(famous)