import urllib.request
import urllib.error
from urllib.parse import urlparse
from bs4 import BeautifulSoup

accepted_scheme = ['http://', 'https://', 'ftp']


def openURL(link):
    web_link = urllib.request.Request(link, data=None, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        handle = urllib.request.urlopen(web_link)
    except urllib.error.HTTPError:
        print("Page unavailable")
        exit()
    return handle


def fileTitleWrite(soup, link):
    fo = open("title.txt", "w")
    fo.write(parse[1]+"\n")
    fo.write(link + "\n")
    fo.write(soup.title.text)
    fo.close()


def fileLinkWrite(soup, parse):
    fo = open("links.txt", "w")
    for link in soup.findAll('a'):
        if 0 <= str(link.get('href')).find(str(parse[1])):
            continue
        else:
            for s in accepted_scheme:
                if 0 <= str(link.get('href')).find(s):
                    fo.write(str(link.get('href')) + "\n")
    fo.close()


link = str(input("Enter link:"))
parse = urlparse(link)
page = openURL(link)
res = page.read()
soup = BeautifulSoup(res, "html.parser")
fileTitleWrite(soup, link)
fileLinkWrite(soup, parse)
