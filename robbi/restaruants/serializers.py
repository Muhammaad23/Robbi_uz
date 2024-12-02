from rest_framework import serializers
from .models import Restaurants, Restaurant_info, Menu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['id', 'title', 'jop_time', 'image', 'address']

class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_info
        fields = ['id', 'jop_time', 'address', 'latitude', 'longitude', 'info', 'tel']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'image', 'price']
