from django.urls import path

from .views import (
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    CommentDetailView,
    ObtainTokenPairWithUserInfoView,
    TokenRefreshWithUserInfoView,
)

urlpatterns = [
    path('token/', ObtainTokenPairWithUserInfoView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshWithUserInfoView.as_view(), name='token_refresh'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
