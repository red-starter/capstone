from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint as p
url = "http://www.utlands.utsystem.edu/ULLease/100001"
response = urlopen(url)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
parcels = soup.find_all('table',class_ = "parcelDetail" )
p(parcels)
docs = soup.find("div", id="docs")
p(docs)

surface = soup.find("div", "data-ng-app"="Surface Acreage")

# LeaseNumber = soup.find("input", id="LeaseNumber")
# p(LeaseNumber)
# CountyName = soup.find("select", id="CountyName")
# p(CountyName)
# ddlLeaseStatus = soup.find("select", id="ddlLeaseStatus")
# p(ddlLeaseStatus)
# ddlLeaseStatus = soup.find("select", id="ddlLeaseStatus")
# p(ddlLeaseStatus)
# ddlBlock = soup.find("select", id="ddlBlock")
# p(ddlBlock)
# ddlSection = soup.find("select", id="ddlSection")
# p(ddlSection)