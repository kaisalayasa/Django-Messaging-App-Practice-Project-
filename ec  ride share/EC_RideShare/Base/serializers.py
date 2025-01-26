from .models import UserMessages,CustomUser,UserListing
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields=['username','email','password','status','bio','profile_pic']


class UserMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserMessages
        fields=['room','user','text']


class UserListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserListing
        fields=['ride_type','user','text']