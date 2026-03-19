import requests
from bs4 import BeautifulSoup

url = "https://thongthai.work"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all(class_ = "blog-entry-inner")
    for tag in a_tags:
        print(tag.text)
else:
    print("error")
    