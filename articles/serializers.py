from rest_framework import serializers
from .models import Comment, Article, Hashtag

class ArticleSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %p %H:%M ")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %p %H:%M ")
    class Meta:
        model = Article
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %p %H:%M ")
    class Meta:
        model = Comment
        fields = "__all__"

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = "__all__"
