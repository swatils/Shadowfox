import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quote blocks
    quotes = soup.find_all('div', class_='quote')

    # Extract and print quotes with authors
    for index, quote in enumerate(quotes, start=1):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"{index}. \"{text}\" - {author}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
