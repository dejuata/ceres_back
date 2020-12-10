from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['pk'])
        product.is_active = False
        product.save()
        return Response(status=status.HTTP_202_ACCEPTED)
