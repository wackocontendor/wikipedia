from bs4 import BeautifulSoup
import requests
import re

#hit random URL
def get_new_link():
    return "https://en.wikipedia.org/wiki/Special:Random"

new_link = get_new_link()
data = requests.get(new_link)

soup = BeautifulSoup(data.text, 'html.parser')
chosen_url = data.url
page_title = soup.find("h1", {"id": "firstHeading"}).text
first_paragraph = str(soup.find("div", {"id": "mw-content-text"}).find('p', class_=None))
remove_parentheses = re.sub(r'\([^)]*\)', '', first_paragraph)
output = BeautifulSoup(remove_parentheses, 'html.parser')

for link in output.find_all('a'):
    parent = link.parent.name
    if parent != 'p':
        continue
    if '/Help:' in link.get('href'): #need to also build in functionality to check for cite references
        continue
    else:
        first_link = link
        break
print(f"Page: {page_title} ({chosen_url})")
print(f"First link: https://en.wikipedia.org{first_link.get('href')}")