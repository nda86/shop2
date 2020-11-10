from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    positions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
