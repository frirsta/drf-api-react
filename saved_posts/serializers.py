from django.db import IntegrityError
from rest_framework import serializers
from .models import SavePost


class SavePostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SavePost
        fields = [
            'id', 'created_date', 'post', 'owner'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible dublicate'
            })
