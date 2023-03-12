from django.db.models import Count
from rest_framework import permissions, filters
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from drf_api.permissions import OwnerOrReadOnly
from .models import Post
from .serializers import PostsSerializer


class PostList(ListCreateAPIView):
    """
    Displays a list of all the posts and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostsSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    Display post detail.
    The owner of the post can edit and delete their post here.
    """
    permission_classes = [OwnerOrReadOnly]
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
