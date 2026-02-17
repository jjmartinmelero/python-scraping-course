
import requests
import re

url = "https://www.apple.com/es/shop/buy-mac/macbook-pro"

response = requests.get(url)


if response.status_code == 200:
    print("success !")


html = response.text

# regex to find the price
price_pattern = r'<span class="as-pricepoint-fullprice">(.*?)</span>'
match = re.search(price_pattern, html)

# print(html)

if match:
    print(f"El precio del producto es: {match.group(1)}")


# get de title if the pattern is FileNotFoundError
title_pattern = r'<title>(.*?)</title>'
match = re.search(title_pattern, html)

if match:
    print(f"El titulo es: {match.group(1)}")
