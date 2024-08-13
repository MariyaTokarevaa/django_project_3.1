from rest_framework import serializers
from main.models import Review, Product


class ProductListSerializer(serializers.ModelSerializer):
    # реализуйте поля title и price
    class Meta:
        model = Product
        fields = ['title', 'price']
class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = ['text', 'mark']

class ProductDetailsSerializer(serializers.ModelSerializer):
    comments= ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'comments']
