from bs4 import BeautifulSoup
import requests


url = "https://www.apple.com/es/shop/buy-mac/macbook-pro"

response = requests.get(url)

if response.status_code == 200:
    print("success !")


soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

title_tag = soup.title

if title_tag:
    print(f"the title is: {title_tag.text}")


metas = soup.title.parent.find_all('meta')
# print(metas)


# find price using bs4
price_span = soup.find('span', class_='as-pricepoint-fullprice')

if price_span:
    print(f"the price is: {price_span}")


# find all the prices
prices_span = soup.find_all('span', class_='as-pricepoint-fullprice')

for price in prices_span:
    print(f"the price is: {price.text}")


# find each product and get the name and the price
products = soup.find_all(class_='rc_productselection_item')

for product in products:
    name = product.find(class_="list-title").text
    price = product.find(class_="rc_prices_fullprice").text
    print(f"The price of {name} is: {price}")
