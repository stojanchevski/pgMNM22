import django
import requests
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from bs4 import BeautifulSoup
from app.models import PostDE
import psycopg2

response = requests.get("https://makedonien-geschichte.blogspot.com/")
soup1 = BeautifulSoup(response.content, "html.parser")
articles1 = soup1.find_all("div", class_="index-post")
articles = []

conn = psycopg2.connect(
    host="localhost",
    database="mnm1",
    user="test1",
    password="admin"
)

cur = conn.cursor()


for article in articles1:
    image = article.find("img")["src"]
    category = soup1.find('span', {'class': 'post-tag index-post-tag'}).text.strip()
    title = article.find("h2", class_="post-title").text.strip()

    short_content = article.find("p").text.strip()
    link = article.find("a")["href"]
    new_post = PostDE(title1=title, link=link, image_link=image, category=category, short_content=short_content)
    articles.append(new_post)
    cur.execute(
        "INSERT INTO app_postde (title1, link, image_link, category, short_content) VALUES (%s, %s, %s, %s, %s)",
        (new_post.title1, new_post.link, new_post.image_link, new_post.category, new_post.short_content)

    )
    conn.commit()

    print(new_post.category)
    print(new_post.title1)

cur.close()
conn.close()

