""" Merlo Posts URL Configuration """
from django.contrib import admin
from django.urls import path

from merlo.posts.views import ListArticles, ListSingleArticle

urlpatterns = [
    path('', ListArticles.as_view()),
    path('<slug:slug>/', ListSingleArticle.as_view()),
]
