from rest_framework import permissions, generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import SavePost
from .serializers import SavePostSerializer


class SavePostList(generics.ListCreateAPIView):
    """
    Displays a list of all the SavePosts and their information.
    The filterset_fields can find Saved Posts made by a specific user
    The filterset_fields can also find what Saved Posts have been made
    on a specific post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavePostSerializer
    queryset = SavePost.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavePostDetail(generics.RetrieveDestroyAPIView):
    """
    Display SavePost detail.
    The owner of the Saved Post can delete their Saved Post here.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = SavePost.objects.all()
    serializer_class = SavePostSerializer
