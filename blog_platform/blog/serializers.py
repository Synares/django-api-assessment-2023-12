# blog/serializers.py
from rest_framework import serializers
# blog/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Post, Comment


class ObtainTokenPairWithUserInfoSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = self.user.username
        return data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

    def validate_content(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Comment must be at least 5 characters long.")
        return value
