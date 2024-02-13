from bs4 import BeautifulSoup
import requests

#hit random URL
def get_new_link():
    return "https://en.wikipedia.org/wiki/Special:Random"

new_link = get_new_link()
data = requests.get(new_link)

chosen_url = data.url

soup = BeautifulSoup(data.text, 'html.parser')

links = soup.find("div", {"id": "mw-content-text"}).find('p', class_=None)

for link in links.find_all('a'):
    parent = link.parent.name
    if parent != 'p':
        continue
    if '/Help:' in link.get('href'): #need to also build in functionality to check for cite references
        continue
    else:
        first_link = link
        break

print(parent)
print(chosen_url)
print("https://en.wikipedia.org" + first_link.get('href'))