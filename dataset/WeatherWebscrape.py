import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

path = os.getcwd()
print("The current directory is %s" % path)

url = 'https://mesonet.agron.iastate.edu/archive/data/2009/'

for i in range(3, 5):
	month = str(i)
	if i < 10:
		month = '0' + month
	os.mkdir(month + "/")

	for l in range(1, 25):
		day = str(l)
		if l < 10:
			day = '0' + day
		os.mkdir(month + "/" + day)
		webURL = url + month + '/' + day + "/GIS/uscomp/"
		response = requests.get(webURL)

		soup = BeautifulSoup(response.text, "html.parser")
		all_a_tags = soup.findAll('a')
		image = 1
		for t in range(len(all_a_tags)):
			link = all_a_tags[t]['href']
			if link[-3:] == 'png' and link[0] == 'n':
				link = webURL + link
				print(link)
				urllib.request.urlretrieve(link, month + "/" + day + "/2009" + '.' + month + '.' + day + '.' + str(image) + '.png')
				image += 1
				time.sleep(1)



response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

one_a_tag = soup.findAll('a')[5]
link = 'https://mesonet.agron.iastate.edu/archive/data/2009/03/05/GIS/uscomp/' + one_a_tag['href']

urllib.request.urlretrieve(link, 'practice.png') 