# @lndgrn's page spider
# v. 1
import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://blog.clindgrencv.com"

# make 2 lists
urls = [url] # 1) stack of urls to scrape
visited = [url] # 2) historical record of urls

while len(urls) > 0:
	try:
		htmltext = urllib.urlopen(urls[0]).read() # the queue
	except:
		print urls[0]
	soup = BeautifulSoup(htmltext)

	urls.pop(0) # pops the first element off of the array
	print len(urls)

	for tag in soup.findAll('a',href=True):
		# function to normalize urls // joining href to top-level domain
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href']) #temp queue of jobs to-be processed
			visited.append(tag['href']) #historical record

print visited