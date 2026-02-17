from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
import requests

parser = argparse.ArgumentParser(description="Web scraping to check SEO for a given URL")
parser.add_argument('url', type=str, help="the url of the site you want scrape and check")

args = parser.parse_args()
url = args.url

# we can use custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.7119.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; http://www.google.com/bot.html)'
}

response = requests.get(url, headers=headers)

print(args.url)

print(response)

if response.status_code == 200:
    print("success !")


soup = BeautifulSoup(response.text, 'html.parser')

print(f"\033[34mReview the page: {url}\033[0m")
print("\n SEO:")

title_page = soup.title.string

if title_page:
    print(f"The title is {title_page}")
    if len(title_page) < 70:
        print("The title has more than 70 characters.")
    else:
        print("The title is too long")


# Extract all h1 elements
titles = [title.text for title in soup.find_all('h1')]

if not titles: 
    print("Titles not found")
elif len(titles) > 1: 
    print("more than 1 title")
    for title in titles:
        print(title)
else:
    print("only 1 title found")