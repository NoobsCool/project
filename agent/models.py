from order.models import *
from django.db import models


# Create your models here.

class Customer(models.Model):
    class Meta:
        verbose_name = "ITW Customer"
        verbose_name_plural = "ITW Customers"
        db_table = "itw_customer"

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    company_name = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
