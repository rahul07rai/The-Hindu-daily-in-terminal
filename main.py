from os import system
import extract as ex
from threading import Thread

def SectionUrl(soup):
    data = {}
    tag = soup.find(id="subnav-tpbar-latest")
    for t in tag.find_all('a'):
        data.update({t.text.lower(): t.attrs['href']})
    return data

def SectionArticleUrl(choiceurl):
    threads = []
    soup = ex.SoupCreate(choiceurl)
    tag = soup.find(class_="archive-list")
    for link in tag.find_all('a'):
        thread = Thread(target=ex.Display, args=(link.get('href'),))
        threads.append(thread)
    for thread in threads:
        thread.start()
        print()
        thread.join()

def menu2(data):
    print("Section List : ")
    for key in list(data.keys()):
        print(key)
    choice = input("Enter Choice : ")
    return choice

def menu1(data):
    choice = menu2(data)
    try:
        SectionArticleUrl(data[choice])
    except KeyError:
        print("Invalid Choice!!!!")
        
def main():
    baseurl = "https://www.thehindu.com/todays-paper/"
    soup = ex.SoupCreate(baseurl)
    data = SectionUrl(soup)
    while True:
        menu1(data)
        print()
        ch = input("Enter any to continue... (Q|q) to quit!!!")
        if ch == 'Q' or ch == 'q':
            break
        else:
            _ = system("clear") #for windows use 'cls'
            continue
   
if __name__ == '__main__':
    main()
