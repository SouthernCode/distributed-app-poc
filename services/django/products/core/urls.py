from rest_framework import routers
from core.views import ProductViewSet, MyProductsViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"my_products", MyProductsViewSet, basename="my_products")
router.register(r"more_products", ProductViewSet, basename="more_products")
