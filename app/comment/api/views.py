"""
CRUD product:
    - SINGLE
    - LIST (create, read, delete)
- read is always available
- create when login
- edit when owner or admin
- delete when owner or admin
"""
from comment.models import Comment
from rest_framework import authentication, generics
from rest_framework.authtoken.models import Token

from .serializers import CommentSerializer

# -------------------- SINGLE --------------------


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.DjangoObjectPermissions]
    authentication = (authentication.TokenAuthentication,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"


class CommentListCreateAPIView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # get token
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
