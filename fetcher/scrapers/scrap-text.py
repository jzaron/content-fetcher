import re
import requests
from bs4 import BeautifulSoup

#url = "http://www.i-programmer.info/babbages-bag/477-trees.html"
# url = "https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error"
url = 'https://blog.codinghorror.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

for script in soup(["script", "style"]):
    script.decompose()

text = re.sub(r'\n+', r'\n', soup.get_text())
print(text)

