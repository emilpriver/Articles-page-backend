from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from merlo.posts.serializers import ArticleSerializer
from merlo.posts.models import Article


class ListArticles(APIView):
    """ List all articles """

    def get(self, request):
        """
        Return a list of all articles.
        """
        data = Article.objects.all()
        serialized_data = ArticleSerializer(data, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


class ListSingleArticle(APIView):
    """ Get singel article """

    def get(self, request, slug):
        """
        Return a list of all users.
        """
        data = get_object_or_404(Article, slug=slug)
        serialized_data = ArticleSerializer(data, many=False).data
        return Response(serialized_data, status=status.HTTP_200_OK)
