from rest_framework import routers
from core.views import ProductViewSet, MyProductsViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"my_products", MyProductsViewSet)
router.register(r"more_products", ProductViewSet)
