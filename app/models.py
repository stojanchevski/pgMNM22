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
    title = models.TextField(max_length=1000)
    link = models.URLField()
    image_link = models.URLField()
    category = models.TextField(max_length=1000)
    short_content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title





class Post(models.Model):
    title1 = models.TextField(max_length=1000)
    link = models.TextField()
    image_link = models.TextField()
    category = models.TextField(max_length=1000)
    short_content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title1


class PostDE(models.Model):
    title1 = models.TextField(max_length=1000)
    link = models.TextField()
    image_link = models.TextField()
    category = models.TextField(max_length=1000)
    short_content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title1


class PdfFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title


class FBTest(models.Model):
    short_content = models.TextField()
    time = models.TextField()

    def __str__(self):
        return self.short_content


class PostENG(models.Model):
    title1 = models.TextField(max_length=1000)
    link = models.TextField()
    image_link = models.TextField()
    category = models.TextField(max_length=1000)
    short_content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title1
