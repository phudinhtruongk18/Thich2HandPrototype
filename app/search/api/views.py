from category.api.serializers import CategorySerializer
from category.models import Category
from rest_framework import generics


class SearchCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):

        query = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        result = Category.objects.none()
        if q is not None:
            owner = None
            if self.request.user.is_authenticated:
                owner = self.request.user
            result = query.search(q, owner=owner)
        return result
