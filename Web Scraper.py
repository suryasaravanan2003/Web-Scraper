import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
quotes = soup.find_all("div", class_="quote")

# Save to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        writer.writerow([text, author])

print("Web scraping complete! Data saved to quotes.csv")
