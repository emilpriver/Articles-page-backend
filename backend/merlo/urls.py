""" Merlo URL Configuration """
from django.urls import path, include

urlpatterns = [
    path('posts/', include('merlo.posts.urls'))
]
