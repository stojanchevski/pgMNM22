from django.contrib import admin
from .models import MyModel, Article, Post, PdfFile
# Register your models here.

admin.site.register(MyModel)
admin.site.register(Article)
admin.site.register(Post)
admin.site.register(PdfFile)
