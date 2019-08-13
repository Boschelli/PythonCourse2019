## Go to https://polisci.wustl.edu/people/88/
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page

from bs4 import BeautifulSoup
import urllib.request
import csv

web_address = 'https://polisci.wustl.edu/people/88/'
web_page = urllib.request.urlopen(web_address)
soup = BeautifulSoup(web_page.read())

# Get Faculty URLS #

links=[]
 test=soup.find_all('a',{'class':'card'}):
for i in test:
	links.append("https://polisci.wustl.edu"+i.get('href'))

# Webscrapping #

results=[]
for faculty in links:
	try:
		webPage=urllib.request.urlopen(faculty)
	except:
		continue
	soup2 = BeautifulSoup(webPage.read())
	try:
		name=soup2.find('h1').get_text()
	except:
		name='N/A'
		pass
	try:
		title=soup2.find('div',{'class':'title'}).get_text()
	except:
		title='N/A'
		pass
	try:
		email=soup2.find('ul',{'class':'detail contact'}).li.get_text()[7:]
	except:
		email='N/A'
		pass
	try:
		website=soup2.find('ul',{'class':'links'}).li.a.get('href')
	except:
		website='N/A'
		pass
	try:
		specialization=soup2.find('div',{'class':'post-excerpt'}).p.get_text()
	except:
		specialization='N/A'
		pass
	results.append([name,title,email,website,specialization])

# Getting Rid of Pesky Unicoding #

for i in results:
	if "\u200b" in i[-1]:
		print('Found one')
		i[-1]=i[-1][1:-1]

# Printing to CSV #

with open('washu_fauclty.csv','w') as f:
	my_writer=csv.DictWriter(f,fieldnames=('Name','Title','Specialization','Email','Webpage'),lineterminator = '\n')
	my_writer.writeheader()
	for faculty in results:
		my_writer.writerow({'Name':faculty[0],'Title':faculty[1],'Specialization':faculty[4],'Email':faculty[2],'Webpage':faculty[3]})
