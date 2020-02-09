from rest_framework import serializers
from merlo.posts.models import Article, Category


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        models: Category


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    content = serializers.CharField()
    thumbnail = serializers.ImageField()
    category = CategorySerializer(many=True)

    class Meta:
        models: Article
