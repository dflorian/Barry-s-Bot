### grab all urls from barry white's lyrics
import requests
import re
import bs4
import markovify

res = requests.get("http://www.allthelyrics.com/lyrics/barry_white")

soup = bs4.BeautifulSoup(res.text)
list_url = []
soup.prettify()
for anchor in soup.findAll('a', href=True):
    if str("/lyrics/barry") in anchor['href'][:20]:
        list_url.append(anchor['href'])

### go through each url of the list & grab lyrics
text_list = []
for url in list_url:
    base = 'http://www.allthelyrics.com'
    res = requests.get(base+url)

    soup = bs4.BeautifulSoup(res.text)
    div = soup.find(id="main")
    div.prettify()

    for anchor in div.findAll('p', href=False):
        text_list.append(anchor)

# to text
text = " ".join(str(x) for x in text_list)
text = text.replace('\n','. ').replace("<p>","").replace("</p>","").replace("<br/>","")
# Build the model.
text_model = markovify.Text(text, state_size=3)
# Print five randomly-generated sentences
for i in range(5):
    if lyrics != None:
        print(text_model.make_sentence())
