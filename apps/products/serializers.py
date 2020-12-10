from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'model', 'serial', 'type_pro', 'date_purchase', 'cost', 'state', 'quantity')
