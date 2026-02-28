import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
all_quotes = []

while True:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    everything = soup.find_all("div", class_="quote")
    for quote in everything:
        quotes = quote.find("span", class_="text").text
        authors = quote.find("small", class_="author").text
        tags = quote.find_all("a", class_="tag")


        tag_list = []

        for tag in tags:
            tag_list.append(tag.text)

        print(quotes)
        print(authors)
        print( ", ".join(tag_list))
        all_quotes.append([quotes, authors, ", ".join(tag_list)])

    next_page = soup.find("li", class_="next")
    if not next_page:
        break
    next_link = next_page.find("a")["href"]
    url = "https://quotes.toscrape.com" + next_link
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Quote", "Author", "Tags"])

    writer.writerows(all_quotes)


