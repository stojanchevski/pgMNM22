import django
import requests
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from bs4 import BeautifulSoup
from app.models import Post
import psycopg2

response = requests.get("https://xn--80axd.xn--d1alf/")
soup1 = BeautifulSoup(response.content, "html.parser")
articles1 = soup1.find_all("div", class_="gridmag-grid-post")
articles = []

conn = psycopg2.connect(
    host="localhost",
    database="test1",
    user="test1",
    password="admin"
)
cur = conn.cursor()

for article in articles1:
    image = article.find("img")["src"]
    categories = article.find('a', attrs={'rel': 'category tag'})
    category = categories.text
    title1 = article.find("h3", class_="gridmag-grid-post-title")
    title = title1.text
    short_content = article.find("p").text
    link = article.find("a")["href"]
    new_post = Post(title1=title, link=link, image_link=image, category=category, short_content=short_content)
    articles.append(new_post)
    cur.execute(
                    "INSERT INTO app_post (title1, link, image_link, category, short_content) VALUES (%s, %s, %s, %s, %s)",
                        (new_post.title1, new_post.link, new_post.image_link, new_post.category, new_post.short_content)

                )
    conn.commit()

cur.close()
conn.close()

