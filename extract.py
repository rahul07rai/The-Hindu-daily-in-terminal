import re
from urllib import request
from bs4 import BeautifulSoup

def SoupCreate(url): 
    html = request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(html, 'lxml')
    return soup

def Title(soup):
    title = soup.title.text.strip('\n')
    return title

def Author(soup):
    try:
        raw = soup.find(class_="auth-nm")
        author = raw.text.strip('\n')
    except AttributeError:
        author = "No Author Field"
    return author

def PlaceDate(soup):
    tag = soup.find_all(class_=re.compile("blue-color"), limit=2)
    place = tag[0].text.strip('\n')
    date = tag[1].text.strip('\n')
    return (place, date)	

def Intro(soup):
    try:
        raw = soup.find(class_="intro")
        intro = raw.text.strip('\n')
    except AttributeError:
        intro = "No Intro Field"
    return intro

def Text(soup):
    try:
        text = []
        tag = soup.find(id=re.compile("content-body"))
        for t in tag.find_all('p'):
            temp = t.text.strip('\n')
            if temp != '':
                text.append(temp)
            else:
                continue
    except AttributeError:
        text.append("No Text field")
    return text

def Display(url):
    soup = SoupCreate(url)
    loc, date = PlaceDate(soup)    
    print("{0} : {1}".format("Title", Title(soup)))
    print("{0} : {1}".format("Author", Author(soup)))
    print("{0} : {1}".format("Location", loc))
    print("{0} : {1}".format("Date", date))
    print("{0} : {1}".format("Intro", Intro(soup)))
    print("{0} : {1}".format("Text", Text(soup)))
