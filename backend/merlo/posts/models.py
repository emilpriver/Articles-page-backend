from django.db import models


class Category(models.Model):
    title = models.TextField(default="")
    slug = models.SlugField(default="", unique=True, blank=False)
    thumbnail = models.ImageField(default="")


class Article(models.Model):
    title = models.TextField(default="")
    slug = models.SlugField(default="", unique=True, blank=False)
    content = models.TextField(default="")
    thumbnail = models.ImageField(default="")
    category = models.ManyToManyField(Category)
