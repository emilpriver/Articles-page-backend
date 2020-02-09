from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from merlo.posts.serializers import ArticleSerializer
from merlo.posts.models import Article


class ListArticles(APIView):
    """ List all articles """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        data = Article.objects.all()
        serialized_data = ArticleSerializer(data, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)
