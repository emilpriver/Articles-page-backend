from django.db import models
from django.utils import timezone


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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Article, self).save(*args, **kwargs)
