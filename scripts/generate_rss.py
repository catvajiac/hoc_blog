#!/usr/bin/env python3

import json
import os
import time

ARTICLES_PATH       = '../json/articles.json'
PLANET_TITLE        = 'hoc_blog'
PLANET_DESCRIPTION  = 'articles for history of computing'
PLANET_URL          = 'https://catvajiac.github.io/hoc_blog/'
POSTS_DIR           = '../pages'

# load existing articles
try:
  articles_json = json.load(open(ARTICLES_PATH))
except IOError:
  articles_json = {}

# Add every entry from every blog feed
for post in os.listdir(POSTS_DIR):
  try:
    name, ext = post.split(".")
  except ValueError:
    continue

  if ext != 'md':
    continue

  entry_id = name[-2:]
  articles_json[entry_id] = {
    'author'    : 'cvajiac',
    'title'     : name,
    'link'      : "{}#{}".format(PLANET_URL, entry_id)
  }


# store articles
with open(ARTICLES_PATH, 'w+') as articles_file:
  json.dump(articles_json, articles_file)

print('''<rss version="2.0">
<channel>
<title>{planet_title}</title>
<link>{planet_url}</link>
<description>
{planet_description}
</description>'''.format(planet_title       = PLANET_TITLE,
                         planet_url         = PLANET_URL,
                         planet_description = PLANET_DESCRIPTION))

for article_id, article in sorted(articles_json.items(), reverse=True):
  print('''<item>
<title>{article_title}</title>
<author>{article_author}</author>
<link>{article_link}</link>
<guid>{article_id}</guid>
</item>'''.format(article_title     = article['title'],
                  article_author    = article['author'],
                  article_link      = article['link'],
                  article_id        = article_id))

print('''</channel>
</rss>''')
