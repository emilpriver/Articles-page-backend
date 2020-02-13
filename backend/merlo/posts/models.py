import json

from django.db import models
from django.utils import timezone

from backend.utils.models import JSONField
from backend.utils.json import json_strip_whitespace


class User(models.Model):
    nickname = models.CharField(max_length=255, default="")
    firstname = models.CharField(max_length=255, default="")
    surname = models.CharField(max_length=255, default="")
    email = models.EmailField(default="", unique=True, blank=False)
    twitter = models.CharField(
        max_length=255, default="", unique=True, blank=True)
    github = models.CharField(
        max_length=255, default="", unique=True, blank=True)
    gitlab = models.CharField(
        max_length=255, default="", unique=True, blank=True)
    avatar = models.ImageField(default="")

    def __str__(self):
        return self.nickname


class Category(models.Model):
    title = models.TextField(default="")
    slug = models.SlugField(default="", unique=True, blank=False)
    thumbnail = models.ImageField(default="")

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.TextField(default="")
    slug = models.SlugField(default="", unique=True, blank=False)
    content = JSONField(default="", null=True, blank=True)
    thumbnail = models.ImageField(default="")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()

        self.version += 1

        self.updated = timezone.now()
        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        if self.author:
            return '%s - %s' % (self.author.nickname, self.title)
        else:
            return self.title
