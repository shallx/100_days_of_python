from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
articles = soup.select(".titleline a")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.string)
    article_links.append(article.get("href"))

article_upvotes = [int(score.string.split()[0]) for score in soup.findAll(class_="score")]
print(article_upvotes)
index = article_upvotes.index(max(article_upvotes))
print(article_upvotes[index])
