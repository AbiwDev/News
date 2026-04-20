from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.PostListCreateAPIView.as_view()),
    path("post/<int:id>/", views.PostDetailAPIView.as_view()),

    path("categories/", views.PostListCreateAPIView.as_view()),
    path("categories/<int:id>/", views.CategoryDetailAPIView.as_view()),

    path("comments/", views.CommentListCreateAPIView.as_view()),
    path("comments/<int:id>/", views.CommentDetailAPIView.as_view()),

    path("like/<int:post_id>/", views.LikeToggleAPIView.as_view()),
]