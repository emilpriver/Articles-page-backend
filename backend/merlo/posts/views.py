from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from merlo.posts.serializers import ArticleSerializer
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
        required_fields = ['title', 'content', 'thumbnail', 'category']
        if all(request.data.get(item) for item in required_fields):

            title = request.data.get('title')
            content = request.data.get('content')
            thumbnail = request.FILES.get('thumbnail')
            category = request.data.get('category')

            category_object = Category.objects.filter(slug=category)
            if not category_object.exists():
                return Response("Category dont exists", status=status.HTTP_400_BAD_REQUEST)

            data = {
                "title": title,
                "content": content,
                "thumbnail": thumbnail,
                "category": category_object.first().__dict__
            }

            serializer = ArticleSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "ok",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Please all required fields", status=status.HTTP_400_BAD_REQUEST)


class ListSingleArticle(APIView):
    """ Get singel article """

    def get(self, request, slug):
        """
        Return a list of all users.
        """
        data = get_object_or_404(Article, slug=slug)
        serialized_data = ArticleSerializer(data, many=False).data
        return Response(serialized_data, status=status.HTTP_200_OK)
