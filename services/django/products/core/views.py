from rest_framework import viewsets, mixins

from core.models import Product
from core.serializers import ProductSerializer
from core.custom_auth import ExternalApiTokenAuthentication


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name", "description"]
    ordering_fields = ["name", "description", "price", "created_at", "updated_at"]
    ordering = ["-created_at"]


class MyProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [ExternalApiTokenAuthentication]

    def get_queryset(self):
        user_id = self.request.user.get("id", None)
        if user_id:
            return Product.objects.filter(user_id=user_id)
        return super().get_queryset()
