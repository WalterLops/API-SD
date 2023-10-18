from rest_framework import serializers
from .models import CadastroDispositivo, Falha
from .models import CustomUser
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class CadastroDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroDispositivo
        fields = '__all__'

class FalhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Falha
        fields = '__all__'
