template==
""extrating the headers from the whole file"""

import urllib
import BeautifulSoup

url="http://www.nytimes.com/?WT.z_jog=1&hF=t&vS=undefined"

con=urllib.urlopen(ur)

soup=BeautifulSoup.BeautifulSoup(con)

all_links=soup.findAll("a")
for link in all_links:
	print link.get("href")



### here searching for all the headers since in HTML headers are denoted by a and then print the links, href denoted by header
