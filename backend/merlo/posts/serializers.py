from rest_framework import serializers
from merlo.posts.models import Article, Category, User


class AuthorSerializer(serializers.Serializer):
    nickname = serializers.CharField(required=False)
    firstname = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    twitter = serializers.CharField(required=False)
    github = serializers.CharField(required=False)
    gitlab = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)

    class Meta:
        models = User


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    slug = serializers.SlugField()
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        models = Category


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField(required=False)
    content = serializers.CharField()
    thumbnail = serializers.ImageField()
    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    author = AuthorSerializer(many=False, read_only=True)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        models = Article
        fields = ['title', 'slug', 'content',
                  'thumbnail', 'category', 'author']

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.slug = validated_data.get('slug', instance.created)
    #     return instance
