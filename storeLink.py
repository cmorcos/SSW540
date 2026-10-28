from urllib.parse import urlparse   # found tool online
from html.parser import HTMLParser

links = []  # list to store links

class LinkFinder(HTMLParser):
    def handle_starttag(self, tag, attrs):  #when python finds html
        if tag == "a":  # check tag for potential hyperlink
            for name, value in attrs:   # look through tag 
                if name == "href":  # find address of website
                    links.append(value)

# open + read html file
file = open("test.html", "r")
html = file.read()
file.close()

finder = LinkFinder()   # create linkfinder from class
finder.feed(html)   # search html

def get_domain(link):    # get domain from link
    return urlparse(link).netloc
links.sort(key=get_domain)  # sort by domain
for link in links:
    print(link)

# github link: 