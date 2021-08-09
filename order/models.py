from django.contrib.auth.models import User
from agent.models import Customer, User
from product.models import Product, Product_category
from django.db import models
from rest_framework.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
def validate_length(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)
    if length > 10:
        raise ValidationError('The value is above 10 digits')


class Counter(models.Model):
    class Meta:
        verbose_name = "ITW Counter"
        verbose_name_plural = "ITW Counters"
        db_table = "itw_counter"

    name = models.CharField(max_length=10)
    value = models.IntegerField

    @property
    def get_name(self):
        self.name = Order.code
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table = "itw_order"

    code = models.CharField(max_length=10, unique=True, null=True)
    code_year = models.IntegerField(validators=[validate_length])
    date_registered = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, related_name='customer_orders', null=True, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='orders', null=True, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.code_year == 2020:
            try:
                c_2020= Order.objects.filter(code_year=2020).latest('id').id+1
            except Order.DoesNotExist:
                c_2020 = 1
            Counter.value = c_2020
            temp_value = f"P - {c_2020} - 2020"
            self.code = temp_value
            super(Order, self).save(*args, **kwargs)

        elif self.code_year == 2021:
            try:
                c_2021= Order.objects.filter(code_year=2021).latest('id').id+1
            except Order.DoesNotExist:
                c_2021 = 1
            Counter.value = c_2021
            temp_value = f"P - {c_2021} - 2021"
            self.code = temp_value
            super(Order, self).save(*args, **kwargs)



class Order_unit(models.Model):
    class Meta:
        verbose_name = "ITW Order Unit"
        verbose_name_plural = "ITW Order Units"
        db_table = "itw_order_unit"

    order = models.ForeignKey(Order, related_name='orderunits', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orderunits_products', null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[validate_length])
    price = models.IntegerField(validators=[validate_length], null=True, blank=True)
