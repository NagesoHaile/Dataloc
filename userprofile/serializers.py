from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id' ,'user_id','profile_picture','birth_date','country','occupation']
        