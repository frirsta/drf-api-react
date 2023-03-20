from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostsSerializer


class PostList(generics.ListCreateAPIView):
    """
    Displays a list of all the posts and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        saved_count=Count('saved', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_date')
    serializer_class = PostsSerializer
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter, DjangoFilterBackend,
                       ]
    filterset_fields = [
        'likes__owner__account',
        'saved__owner__account',
    ]
    ordering_fields = [
        'likes_count',
        'saved_count',
        'comments_count',
    ]
    search_fields = [
        'owner__username',
        'caption',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display post detail.
    The owner of the post can edit and delete their post here.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        saved_count=Count('saved', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_date')
    serializer_class = PostsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = [
        'likes_count',
        'saved_count',
        'comments_count',
    ]
    search_fields = [
        'owner__username',
        'caption',
    ]
