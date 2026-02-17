from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
import requests

parser = argparse.ArgumentParser(description="Web scraping to check SEO for a given URL")
parser.add_argument('url', type=str, help="the url of the site you want scrape and check")

args = parser.parse_args()
url = args.url

url = "https://es.wikipedia.org/wiki/Web_scraping"

# we can use custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.7119.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; http://www.google.com/bot.html)'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("success !")
