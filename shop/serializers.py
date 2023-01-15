from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = '__all__'
        read_only_fields = ['profile', 'category']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ['profile', 'item']

