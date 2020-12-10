from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
