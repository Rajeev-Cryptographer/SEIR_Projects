import requests
from bs4 import BeautifulSoup
import sys

url= sys.argv[1]
if not url.startswith("http"):
    url = "https://" + url
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
res= requests.get(url,headers=headers)
if(res.status_code!=200):
    if res.status_code>=400 and res.status_code<500:
        print("issue on client side")
        exit()
    if res.status_code>=500:
        print("issue on server side")
        exit()
soup=BeautifulSoup(res.text, 'html.parser')
if soup.title:
    print(soup.head.title.get_text())
print('\n')
if soup.body:
    print(soup.body.get_text())
print('\n')

links= soup.find_all('a')
for link in links:
    print(link.get('href'))



