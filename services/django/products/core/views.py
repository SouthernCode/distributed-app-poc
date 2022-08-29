from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.models import Product
from core.serializers import ProductSerializer, CreateProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    ProductViewSet is a viewset that provides the standard actions
    list, create, retrieve, update and destroy.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name", "description", "price", "created_at", "updated_at"]
    ordering = ["-created_at"]

    def get_permissions(self):
        """Only authenticated users can create or update products"""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_serializer_class(self):
        """If we are creating a product, use the CreateProductSerializer"""
        if self.action in ["create", "update", "partial_update"]:
            return CreateProductSerializer
        return ProductSerializer


class MyProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        if user_id:
            return Product.objects.filter(user_id=user_id)
        return super().get_queryset()
