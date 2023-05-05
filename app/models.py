from django.db import models

# Create your models here.
from django.db import models


class MyModel(models.Model):
    # Add fields for your model
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()

    # ...

    # Define a string representation for your model
    def __str__(self):
        return self.field1


class Article(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    image_link = models.URLField()
    category = models.CharField(max_length=200)
    short_content = models.CharField()

    def __str__(self):
        return self.title
