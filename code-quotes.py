# @lndgrn's Code.org spider
# v. 1
import urllib2, re
from BeautifulSoup import BeautifulSoup 

turl = "http://code.org/quotes"
toppage = urllib2.urlopen(turl)
codeSoup = BeautifulSoup(toppage)

nameDivTag = codeSoup.findAll("div", {"class":re.compile("field-name-field-source-name")})
qtDivTag = codeSoup.findAll("div", {"class":re.compile("field-name-field-quote")})

for name,quote in zip(nameDivTag,qtDivTag):
	print name.text
	print quote.text
	print '\n'