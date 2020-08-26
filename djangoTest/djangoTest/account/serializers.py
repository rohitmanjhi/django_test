from rest_framework import serializers
from djangoTest.account.models import User
import re


class SeriesSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    value_of_x = serializers.IntegerField()
    value_of_n = serializers.IntegerField()


class EquationSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    value_of_x = serializers.IntegerField()
    value_of_y = serializers.IntegerField()
    value_of_a = serializers.IntegerField()
    value_of_b = serializers.IntegerField()


class NextNumberSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    value_of_nth = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'mobile', 'password')

    def validate_mobile(self, mobile):
        if re.match(r'[6789]\d{9}$', mobile):
            return mobile
        else:
            raise serializers.ValidationError(
                "Please enter valid mobile number")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
