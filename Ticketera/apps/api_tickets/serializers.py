from rest_framework import serializers
from .models import Issue, Responsible,Issuer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class IssueSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()  # obtiene el usuario logueado
    # )

    class Meta:
        model = Issue
        fields = '__all__'


class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = '__all__'


class Issuer(serializers.ModelSerializer):
    class Meta:
        model = Issuer
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # write only es para que no nos devuelva el password cuando la creee
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])

        user.save()
        Token.objects.create(user=user)
        return user
