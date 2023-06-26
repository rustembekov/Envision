from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = User
        fields = ["username", "email", "password"]

