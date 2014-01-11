# @lndgrn's Code.org spider
# v. 1
import urllib2, re
from BeautifulSoup import BeautifulSoup 

turl = "http://code.org/quotes"
toppage = urllib2.urlopen(turl)
codeSoup = BeautifulSoup(toppage)

nameDivTag = codeSoup.findAll("div", {"class":re.compile("field-name-field-source-name")})
qtDivTag = codeSoup.findAll("div", {"class":re.compile("field-name-field-quote")})

with open("code-quotes.txt", "w") as cq:
	for name,quote in zip(nameDivTag,qtDivTag):
		cq.write(name.text.encode('utf8') + '|')
		cq.write(quote.text.encode('utf8'))
		cq.write("\n\n")
cq.close