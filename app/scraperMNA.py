import django
import requests
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from bs4 import BeautifulSoup
from app.models import Article

response = requests.get("https://xn--80axd.xn--d1alf/")
soup1 = BeautifulSoup(response.content, "html.parser")
articles1 = soup1.find_all("div", class_="gridmag-grid-post")
articles = []

for article in articles1:
    image = article.find("img")["src"]
    categories = article.find('a', attrs={'rel': 'category tag'})
    category = categories.text.strip()
    title1 = article.find("h3", class_="gridmag-grid-post-title")
    title = title1.text.strip()
    short_content = article.find("p").text.strip()
    link = article.find("a")["href"]
    new_post = Article(title, link, image, category, short_content)
    articles.append(new_post)

    featured_article = articles[0]
for art in articles:
    print(art.title)
