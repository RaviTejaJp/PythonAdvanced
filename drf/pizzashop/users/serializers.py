from django.contrib.auth.models import User, Permission
from rest_framework import serializers
from cart.models import Cart


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ["url", "name"]


# User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        Cart.objects.create(user=user)  # Create a cart for the new user
        return user

    def validate(self, attrs):
        breakpoint()
        return super().validate(attrs)
