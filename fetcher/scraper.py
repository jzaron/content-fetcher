"""
@author: jzaron
"""

#TODO: error handling (wrong URL, no access, etc.)

import re
import requests
from bs4 import BeautifulSoup

def get_image_urls(site):
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]

    for url in urls:
        filename = re.search(r'/([^/]*[.](jpg|JPG|gif|GIF|png|PNG))$', url)
        if re.match(r'^//', url):
            url = 'http:' + url
        if not re.match(r'^http', url):
            url = '{}{}'.format(site, url)
        if filename:
            yield url

def get_text(site):
    html = requests.get(site).text
    soup = BeautifulSoup(html, 'html.parser')

    for script in soup(["script", "style"]):
        script.decompose()
        
    return re.sub(r'\n+', r'\n', soup.get_text())