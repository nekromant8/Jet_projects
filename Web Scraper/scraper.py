import requests
import os
from bs4 import BeautifulSoup

def save_articles_on_page(the_article_type, dir_name, url):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("article")
    article: object
    for article in articles:
        article_type = article.find('span', "c-meta__type").text
        if article_type == the_article_type:
            url = article.find('a').get('href')
            a_r = requests.get("https://www.nature.com" + url)
            a_soup = BeautifulSoup(a_r.content, "html.parser")
            a_title = a_soup.title.text
            punct = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            file_name = ''
            for char in a_title:
                if char not in punct:
                    file_name = file_name + char
            file_name = file_name.replace(" ", "_") + ".txt"
            file_name = file_name.replace("__Research_Highlights", "")
            a_body = a_soup.find('div', class_='article-item__body')
            text = a_body.text.strip()
            file = open(dir_name + '/' + file_name, "w", encoding="UTF-8")

            file.write(text)
            file.close()

n_pages = int(input())
articles_type = input()
for n in range(n_pages):
    dir_name = f'Page_{n + 1}'
    url = f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&Page={n + 1}'
    save_articles_on_page(articles_type, dir_name, url)
print("Saved all articles.")

