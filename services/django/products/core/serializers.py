from core.models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "user_id",
            "name",
            "description",
            "price",
            "image",
            "created_at",
            "updated_at",
            "quantity",
        ]
