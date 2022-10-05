import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.title)
# print(soup.find_all('div'))
# print(soup.find('div'))
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.find(id='score_33052441'))

# print(soup.select('.titleline')[0])
# print(soup.select('.titleline')[0].getText())
# NOTE: getText() OR get_text works same.

# print(soup.select('.score')[0].get_text)

print(soup.select('.titleline')[1]['href'])
