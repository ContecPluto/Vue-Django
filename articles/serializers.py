from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %p %H:%M ")
    class Meta:
        model = Comment
        fields = "__all__"
