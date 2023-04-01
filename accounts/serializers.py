from rest_framework import serializers
from .models import Account
from followers.models import Followers


class AccountsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    following_count = serializers.ReadOnlyField()
    followed_count = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Followers.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Account
        fields = ['owner', 'id', 'created_date',
                  'updated_date', 'bio', 'profile_image', 'is_owner',
                  'posts_count', 'followed_count',
                  'following_count', 'following_id'
                  ]
