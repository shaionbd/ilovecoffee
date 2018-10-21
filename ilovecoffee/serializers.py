from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import serializers, exceptions
from .models import Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class UserSerializerWithHMS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username', 'email')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                # active deactive check
                data['user'] = user
            else:
                msg = "Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both"
            raise exceptions.ValidationError(msg)

        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'no_of_coffee', 'location', 'is_canceled', 'create_at')


class OrderSerializerWithHMS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('url', 'user', 'no_of_coffee', 'location', 'is_canceled', 'create_at')

