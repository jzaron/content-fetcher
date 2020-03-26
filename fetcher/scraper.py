"""
@author: jzaron
"""

#TODO: still cases returned image URL is invalid
#TODO: error handling (wrong URL, no access, etc.)

import re
import requests
from bs4 import BeautifulSoup

def get_image_urls(site):
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    base_url = re.sub(r'/[^/]*$', '/', site)
    paths = [img['src'] for img in img_tags]
    for path in paths:
        filename = re.search(r'/?([^/]*[.](jpg|JPG|gif|GIF|png|PNG))$', path)
        url = path
        if re.match(r'^//', path):
            url = 'http:' + path
        if not re.match(r'^http', path):
            url = f'{base_url}{path}'
        if filename:
            yield url

def get_text(site):
    html = requests.get(site).text
    soup = BeautifulSoup(html, 'html.parser')

    for script in soup(["script", "style"]):
        script.decompose()
        
    return re.sub(r'\n+', r'\n', soup.get_text())