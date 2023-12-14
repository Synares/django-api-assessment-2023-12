# blog/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, ObtainTokenPairWithUserInfoSerializer


class ObtainTokenPairWithUserInfoView(TokenObtainPairView):
    serializer_class = ObtainTokenPairWithUserInfoSerializer


class TokenRefreshWithUserInfoView(TokenRefreshView):
    serializer_class = ObtainTokenPairWithUserInfoSerializer


class PostListCreateView(generics.ListCreateAPIView):
    """
    List and create blog posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete blog posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class CommentListCreateView(generics.ListCreateAPIView):
    """
    List and create comments on post
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete comments on post
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
