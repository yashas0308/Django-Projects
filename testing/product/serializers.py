from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'desc', 'price', 'offers']


class UserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwagrs = {
            'password' : {'write_only' : True}
        }
    
    def save(self):
        account = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Password Must Match.'})
        account.set_password(password)
        account.save()
        return account