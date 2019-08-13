from bs4 import BeautifulSoup
import urllib.request
import csv

# Grabs/Formats all petition hyperlinks from main petition webpage
# roughList: Main petition page
def getLinks(roughList):
    links=[]
    for i in roughList:
        links.append("https://petitions.whitehouse.gov"+i.a.get('href'))
    return links

# Scrapes individual petition page for various info
# url: Petition url
def scrapePetition(url):

    # Opens petition specific webscraper
    webPage = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(webPage.read(),features='html.parser')

    # Grabs title
    title=soup2.find('h1').get_text()

    # Grabs date
    date=soup2.find('h4').get_text()[19:]

    # Grabs signature count
    signatures=soup2.find('span',{'class':'signatures-number'}).get_text()

    # Grabs list of issue tags
    #issueAreas=soup2.find('div',{"class" :"field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags"}).div.contents
    # Turns list of tags into formatted string
    tags=''
    for i in soup2.find('div',{"class" :"field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags"}).div.contents:
        tags+=i.get_text()+', '
    # Removes final comman and space
    tags=tags[:-2]

    # Trys to get summary text
    summary=''
    try:
        # Iterates over potential paragraph bodies
        for i in soup2.find('div',{"class" :"field-item"}).find_all('p'):
            summary+=i.get_text()+' '
        # Removes string on the very end
        summary=summary[:-1]
    # Fails if no summary is provided
    except:
        pass

    return [title,date,summary,tags,signatures]

# Opens CSV Writer
with open('whitehouse_petitions.csv','w') as f:
  my_writer=csv.DictWriter(f,fieldnames=('Title','Publication Date','Summary','Issue Tags','Signatures'),lineterminator = '\n')
  my_writer.writeheader()

  # Opens primary webscraper
  web_address = 'https://petitions.whitehouse.gov/petitions?page=1'
  web_page = urllib.request.urlopen(web_address)
  soup = BeautifulSoup(web_page.read(),features='html.parser')
  print('Starting Web Scarping...')

  # Grabs first page of petition hyper links
  tempList=soup.find_all('h3')[3:]

  # Checks if page has any petitions
  while tempList != []:
      # Formats petition links
      links=getLinks(tempList)
      # Loops of formatted links and writes to CSV
      for item in links:
          # Scraps petition link
          temp=scrapePetition(item)
          # Tries to write to CSV
          try:
              my_writer.writerow({'Title':temp[0],'Publication Date':temp[1],'Summary':temp[2],'Issue Tags':temp[3],'Signatures':temp[4]})
          # Catches any encoding errors due to special characters
          except:
             my_writer.writerow({'Title':'ENCODING ERROR'})
             pass

      # Adjusts address to next page number
      web_address=web_address[:-1]+str(int(web_address[-1])+1)

      # Reopens main webscraper
      web_page = urllib.request.urlopen(web_address)
      soup = BeautifulSoup(web_page.read(),features='html.parser')

      # Grabs page of petition hyper links
      tempList=soup.find_all('h3')[3:]
      print("Running...")
print("Finished!")



web_address = 'https://petitions.whitehouse.gov/petitions?page=1'
web_page = urllib.request.urlopen(web_address)
soup = BeautifulSoup(web_page.read(),features='html.parser')


 # Grabs first page of petition hyper links
 tempList=soup.find_all('h3')[3:]
