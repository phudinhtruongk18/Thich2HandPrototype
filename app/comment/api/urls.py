from django.urls import path

from .views import CommentDetail, CommentListCreateAPIView

urlpatterns = [
    path("edit/<int:pk>/", CommentDetail.as_view(), name="comment_detail"),
    path("create/", CommentListCreateAPIView.as_view(), name="comment_create"),
]
