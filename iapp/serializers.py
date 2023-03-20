from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_phone', 'user_name', 'user_lang']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id']


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class RowSerializer(serializers.ModelSerializer):
    sector = SectorSerializer()

    class Meta:
        model = Row
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    row = RowSerializer()

    class Meta:
        model = Place
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class CallsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calls
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = '__all__'

