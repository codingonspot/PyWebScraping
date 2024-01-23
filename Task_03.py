import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}

URL = "https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/"

webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "html.parser")

names = soup.find_all("a", class_="itemName")
prices = soup.find_all("span", class_="itemPrice")

menu = {}

for name, price in zip(names, prices):
    item_name = name.text.strip()
    item_price = price.text.strip()

    if item_name not in menu:
        menu[item_name] = item_price

csv_filename = 'Eatfit_menus.csv'

try:
    with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Item Name', 'Item Price'])

        for item_name, item_price in menu.items():
            writer.writerow([item_name, item_price])
    print(f"Data saved to {csv_filename} successfully.")
except IOError:
    print(f"Failed to write to {csv_filename}.")
