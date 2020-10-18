
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
import pandas as pd

# Init
newsapi = NewsApiClient(api_key='fb11d84c123e491983028590e5bdd0e6')

# /v2/top-headlines
health_headlines = newsapi.get_top_headlines(country='au',
                                          page_size=1, page=1, category='health')
general_headlines = newsapi.get_top_headlines(country='au',
                                          page_size=1, page=1, category='general')


# /v2/everything
# all_articles = newsapi.get_everything(q='politics',
#                                       from_param=date.today(),
#                                       language='en', page_size=10, page=2)
#
# # /v2/sources
# sources = newsapi.get_sources()
#print(json.dumps(all_articles, indent=6))


sd = SortedDict()
newsList = []    #actual unordered return list
textList = []
urlList = []

print("# Health Articles: " + str(health_headlines['totalResults']))
print("# General Articles: " + str(general_headlines['totalResults']))

all_headlines = health_headlines['articles'] + general_headlines['articles']
i = 0

for article in all_headlines:
    i += 1
    print(str(i) + ". " + article['url'])
    url = Request(article['url'], headers={'User-Agent': 'Mozilla/5.0'})

    html = None
    try:
        html = urlopen(url)
    except OSError:
        continue

    if "nytimes" in article['url'] or "wsj" in article['url'] or "news.google.com" in article['url'] or "subscribe" in article['url']:
        continue

    if [article['url'], article['publishedAt']] not in newsList:
        newsList.append([article['url'], article['publishedAt']])
        urlList.append(article['url'])
    else:
        continue


    soup = BeautifulSoup(html, "html.parser")
    decoding = soup.original_encoding

    decoded = urlopen(url).read().decode(decoding)
    text = get_text(decoded)
    textList.append(text)


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

i = 1

print("\nlength: " + str(len(sd.keys())))
for key in sd:
    print(str(i) + ". " + sd[key] + ": " + str(key))
    i += 1


print("result lengths:")
print(len(all_headlines))
print(len(newsList))
for news in newsList:
    print("URL: " + news[0] + " |Date: " + news[1])

url_list = pd.Series(urlList, name='url')
text_list = pd.Series(textList, name='article_text')

df = pd.merge(url_list, text_list, left_index=True, right_index=True)
df.to_csv('article_ranking_data.csv')






