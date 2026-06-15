import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])

        for product in products:
            title = product.h3.a["title"]
            price = product.find("p", class_="price_color").text

            writer.writerow([title, price])

    print("Data berhasil disimpan ke products.csv")

else:
    print("Gagal mengakses website")