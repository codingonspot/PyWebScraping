import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

URL = "https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/"

webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "html.parser")

r = requests.get(URL)

names = soup.find_all("a", class_="itemName")

prices = soup.find_all("span", class_="itemPrice")

l = len(names)

for i in range(l):
    print(names[i].text, end=' ')
    print(prices[i].text, end='\n')

