from django.db import models


# Create your models here.

class Product_category(models.Model):
    class Meta:
        verbose_name = "ITW Product Category"
        verbose_name_plural = "ITW Product Categories"
        db_table = "itw_product_category"

    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "ITW Product"
        verbose_name_plural = "ITW Products"
        db_table = "itw_product"

    name = models.CharField(max_length=50, null=True)
    default_price = models.FloatField(max_length=10, null=True)
    description = models.CharField(max_length=50, null=True)
    deleted = models.BooleanField(default=False, null=True)
    product_category = models.ManyToManyField(Product_category, related_name="products")

    def __str__(self):
        return self.name

