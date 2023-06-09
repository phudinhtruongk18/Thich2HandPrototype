from django.urls import include, path

from .views import delete_comment, submit_comment

urlpatterns = [
    path("submit_comment/<int:product_id>/", submit_comment, name="submit_comment"),
    path("delete_comment/<int:comment_id>/", delete_comment, name="delete_comment"),
    path("api/", include("comment.api.urls")),
]
