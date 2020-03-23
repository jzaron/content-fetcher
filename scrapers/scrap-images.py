import re
import requests
from bs4 import BeautifulSoup

#site = 'http://pixabay.com'
#site = 'https://www.i-programmer.info/babbages-bag/477-trees.html'
site = 'https://en.wikipedia.org/wiki/Wikipedia'
# site = 'https://blog.codinghorror.com/'
# site = 'https://stackoverflow.com/questions/18408307/how-to-extract-and-download-all-images-from-a-website-using-beautifulsoup'

response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]

for url in urls:
    filename = re.search(r'/([^/]*[.](jpg|JPG|gif|GIF|png|PNG))$', url)
    print(url)
    if re.match(r'^//', url):
        url = 'http:' + url
    if not re.match(r'^http', url):
        # sometimes an image source can be relative 
        print('OPS')
        url = '{}{}'.format(site, url)
    print(url)
    if filename:
        with open('images/' + filename.group(1), 'wb') as f:
            print(filename.group(1))
            response = requests.get(url)
            f.write(response.content)
    else:
        print('Unknown file format')
