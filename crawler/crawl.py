import sys
import urllib2
import urlparse
from BeautifulSoup import *

def main(link):
    print "IN MAIN"
    crawlList = set([])
    crawledList = set([])

    crawlList.add(link)

    while 1:
        try:
            page = crawlList.pop()
            print page
        except KeyError:
            raise StopIteration

        try:
            webPage = urllib2.urlopen(page)
            crawledList.add(page)
    
        except:
            print "Could not open Page: ", page
            continue;

        webpage = webPage.read()
        soap = BeautifulSoup(webpage)
        print "SOUP FOLLOWS: "
        print soap
        print "SOUP ENDS"
        links = soap('a')
        for link in links:
            if ('href' in dict(link.attrs)):
                print link['href']
                page = urlparse.urljoin(webPage, link['href'])
                print "PAGE: ",page
            
            if page.find("'") != 1:
                continue

            page = page.split('#')[0] 
            print page
            
            if page[0:4] == 'http' and page not in crawledList:
                print "add this page ot crawl list"
                crawlList.add(links)


if __name__ == "__main__":
    main(sys.argv[1])
