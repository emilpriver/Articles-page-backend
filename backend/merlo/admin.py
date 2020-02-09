""" Merlo Admin """
# import global from django
from django.contrib import admin

# import from local app
from merlo.posts.models import Article, Category

# Regsiter to admin
admin.site.register(Article)
admin.site.register(Category)
