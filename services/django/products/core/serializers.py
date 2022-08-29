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


class CreateProductSerializer(ModelSerializer):
    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        'user_id' is a required field, so we need to get the user_id from the request
        this field is passed in the request body as a json object by the authentication service
        """
        validated_data["user_id"] = self.context["request"].user.id
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "image",
            "quantity",
        ]
        read_only_fields = ["id", "user_id", "created_at", "updated_at"]
