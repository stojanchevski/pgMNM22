# import the necessary libraries and models
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Post, PostDE
from app.UniversalPost import UniversalPost

# query all data from the models
model1_data = Post.objects.all()
model2_data = PostDE.objects.all()


# print the data
all_data = []
for data in model2_data:
    up = UniversalPost(data.title1,data.image_link,data.short_content,data.link,data.category)
    all_data.append(up)

for data in model1_data:
    up = UniversalPost(data.title1, data.image_link, data.short_content, data.link, data.category)
    all_data.append(up)


