from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Account
from .serializers import AccountsSerializer


class AccountList(generics.ListAPIView):
    """
    Displays a list of all the accounts and their information.
    Filterset_fields Can find who follows a specific user.
    The filterset_fields can also find what accounts are
    followed by a specific user.
    """
    queryset = Account.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        following_count=Count(
            'owner__following', distinct=True),
        followed_count=Count('owner__followed', distinct=True)
    ).order_by('-created_date')
    serializer_class = AccountsSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
        ]
    ordering_fields = [
        'posts_count',
        'following_count',
        'followed_count',
        ]
    filterset_fields = [
        'owner__following__followed__account',
        'owner__followed__owner__account',
        ]
    search_fields = ['owner__username']


class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    Display account detail.
    The owner of the account can edit and delete their account here.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        following_count=Count(
            'owner__following', distinct=True),
        followed_count=Count('owner__followed', distinct=True)
    ).order_by('-created_date')
    serializer_class = AccountsSerializer
