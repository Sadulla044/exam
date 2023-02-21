from rest_framework import serializers
from product.models import (
    Category,
    Customer,
    Inventory,
    Order,
    Product,
    ProductImages
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = (
            'date_created',
            'date_updated',
            'slug',
            'id'
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = (
            'date_created',
            'date_updated',
            'slug',
            'id'
        )


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = (
            'date_created',
            'date_updated',
            'slug',
            'id'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = (
            'date_created',
            'date_updated',
            'slug',
            'id'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = (
            'date_created',
            'date_updated',
            'slug',
            'id'
        )


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'
        read_only_fields = (
            'date_created',
            'date_updated',
            'slug',
            'id'
        )