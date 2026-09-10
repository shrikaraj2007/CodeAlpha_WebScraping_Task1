import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text.strip().replace("Â£", "£")
    availability = book.select_one(".availability").text.strip()

    books.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

df = pd.DataFrame(books)

df.to_csv("books_dataset.csv", index=False)

print("Scraping completed!")
print(df)