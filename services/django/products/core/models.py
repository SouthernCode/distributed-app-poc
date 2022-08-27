from django.db import models

# Create your models here.
class Product(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    """User that created the product, lives in the Users microservice"""
    name = models.CharField(max_length=100, null=False, blank=False)
    """Name of the product"""
    description = models.TextField(null=False, blank=False)
    """Description of the product"""
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    """Price of the product"""
    image = models.CharField(max_length=255, null=False, blank=False)
    """File name of the product's image"""
    created_at = models.DateTimeField(auto_now_add=True)
    """Date and time of the product's creation"""
    updated_at = models.DateTimeField(auto_now=True)
    """Date and time of the product's last update"""
    quantity = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]
