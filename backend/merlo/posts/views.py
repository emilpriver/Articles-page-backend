from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from merlo.posts.serializers import ArticleSerializer, CategorySerializer
from merlo.posts.models import Article, Category


class ListArticles(APIView):
    """ List all articles """

    def get(self, request):
        """
        Return a list of all articles.
        """
        data = Article.objects.all()
        serialized_data = ArticleSerializer(data, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        """ Save data """
        title = request.data.get('title')
        content = request.data.get('content')
        thumbnail = request.FILES.get('thumbnail')
        category = request.data.get('category')
        category_object = get_object_or_404(Category, slug=category)

        data = {
            "title": title,
            "content": content,
            "thumbnail": thumbnail,
            "category_id": category_object.id,
            "author_id": 1  # Id of author will be 1 until autentication is implemented
        }

        serializer = ArticleSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            new_post_data = serializer.data
            return Response({
                'status': 'ok',
                'data':  {
                    'title': new_post_data['title'],
                    'slug': new_post_data['slug'],
                    'thumbnail': new_post_data['thumbnail']
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListSingleArticle(APIView):
    """ Get singel article """

    def get(self, request, slug):
        """
        Return a list of all users.
        """
        data = get_object_or_404(Article, slug=slug)
        serialized_data = ArticleSerializer(data, many=False).data
        return Response(serialized_data, status=status.HTTP_200_OK)
