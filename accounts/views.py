from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from drf_api.permissions import OwnerOrReadOnly
from .models import Account
from .serializers import AccountsSerializer


class AccountList(ListAPIView):
    """
    Displays a list of all the accounts and their information.
    Filterset_fields Can find who follows a specific user.
    The filterset_fields can also find what accounts are
    followed by a specific user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AccountsSerializer
    queryset = Account.objects.all()


class AccountDetail(RetrieveUpdateAPIView):
    """
    Display account detail.
    The owner of the account can edit and delete their account here.
    """
    permission_classes = [OwnerOrReadOnly]
    serializer_class = AccountsSerializer
    queryset = Account.objects.all()
