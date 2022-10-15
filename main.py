import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('small', class_='author')

print(quotes)

# for qut in quotes:
#     print(qut.text)
