from rest_framework import serializers
from bangazonapi.models import User


class UserSerializer(serializers.ModelSerializer):
    """json serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'uid',
                  'registered_on',
                  'profile_image_url',
                  'username')
