from django.urls import include, path

from .views import SearchCategoryListView

urlpatterns = [
    path("category/", SearchCategoryListView.as_view(), name="search-category-list"),
]
