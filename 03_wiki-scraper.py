from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests


url = "https://es.wikipedia.org/wiki/Web_scraping"

# we can use custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.7119.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; http://www.google.com/bot.html)'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("success !")

soup = BeautifulSoup(response.text, 'html.parser')

# find all h1 elements
titles = [title.string for title in soup.find_all('h1')]

print(titles)


# extract all <a> elements
links = [urljoin(url, link.get('href')) for link in soup.find_all('a')]

print(links)

# extract all content
# all_text = soup.get_text()
# print(all_text)

# extract text from main elements
# main_text = soup.find('main').get_text()
# print(main_text)

# extract content with an ID
# content_text = soup.find('div', {'id': 'mw-content-text'}).get_text()
# print(content_text)


# Open graph -------------------------------------------------------

url = "https://midu.dev"

# we can use custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.7119.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; http://www.google.com/bot.html)'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("success !")


# extract open graph if exist
og_image = soup.find('meta', {'property': 'og:image'})

# alternative
og_image = soup.find('meta', property='og:image')

if og_image:
    print(og_image['content'])
else:
    print('Image not found')