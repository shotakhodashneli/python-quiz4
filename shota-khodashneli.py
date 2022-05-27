import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

f = open("smartphones.csv", 'w', encoding="utf-8", newline="\n")
file = csv.writer(f)
file.writerow(["Title", "Price", "URL"])
headers = {"Accept-Language": "en-US"}

page = 1

while page < 6:
    try:
        url = f"https://alta.ge/smartphones-page-{page}.html"
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")
        grid_list = soup.find("div", {"class": "grid-list"})
        smartphones = grid_list.find_all("div", {"class": "ty-column3"})

        for each in smartphones:
            title = each.find("a", {"class": "product-title"}).text
            price = each.find("span", {"class": "ty-price-num"}).text
            image_url = each.find("img", {"class": "ty-pict"}).attrs.get("src")
            file.writerow([title, price, image_url])
    except:
        print("")
    page += 1
    sleep(5)