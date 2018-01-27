import Scrape
import Compare


def checkDomain():
    fo = open('title.txt')
    link = fo.readline()
    fo.close()
    return Compare.check(link)


def checkLinks():
    fo = open('links.txt')
    for line in fo:
        link = Scrape.getStrippedLink(line)
        if not Compare.check(link):
            return False
    return True


Scrape.starter()
if checkDomain():
    if checkLinks():
        print("This site is not a fake news site")
    else:
        print("This site has sources from a fake site")
else:
    print("This site is a fake news site")