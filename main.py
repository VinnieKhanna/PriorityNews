
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import date
import readability
import json
from newsapi import NewsApiClient
import requests
from urllib.request import urlopen, Request
from urllib import error
from bs4 import BeautifulSoup
from sortedcontainers import SortedDict
from inscriptis import get_text


# Init
newsapi = NewsApiClient(api_key='fb11d84c123e491983028590e5bdd0e6')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(country='au',
                                          page_size=10,
                                          category='general')

# /v2/everything
all_articles = newsapi.get_everything(q='politics',
                                      from_param=date.today(),
                                      language='en', page_size=10, page=2)

# /v2/sources
sources = newsapi.get_sources()

#print(json.dumps(all_articles, indent=6))

sd = SortedDict()

for article in all_articles['articles']:
    print(article['url'])
    url = Request(article['url'], headers={'User-Agent': 'Mozilla/5.0'})

    html = None
    try:
        html = urlopen(url)
    except OSError:
        continue

    if "nytimes" in article['url'] or "wsj" in article['url']:
        continue
    soup = BeautifulSoup(html, "html.parser")
    decoding = soup.original_encoding

    decoded = urlopen(url).read().decode(decoding)
    text = get_text(decoded)

    # print(text)

    # url = Request(article['url'], headers={'User-Agent': 'Mozilla/5.0'})
    # html = urlopen(url).read()
    # beautify = BeautifulSoup(html, "html.parser")
    #
    # specificEncoding = beautify.original_encoding
    # articleText = beautify.decode(specificEncoding)
    #
    # txt = articleText.get_text()

    readingStats = readability.getmeasures(text, lang='en')
    fleschScore = readingStats['readability grades']['FleschReadingEase']


    sd[fleschScore] = article['url']


print("length" + str(len(sd.keys())))
for key in sd:
    print (sd[key] + ": " + str(key))

print("\nAustralian Specific:\n")
for article in top_headlines['articles']:
    print(article['url'])
    # print(article['urlToImage'])
print(top_headlines['totalResults'])






