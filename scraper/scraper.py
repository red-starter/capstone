from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://www.utlands.utsystem.edu/WellLibrary/LeaseSearch"
response = urlopen(url)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')