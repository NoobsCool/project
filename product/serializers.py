from rest_framework import serializers

from product.models import Product,Product_category


class ProductSerializer(serializers.ModelSerializer):

    product_category = serializers.SlugRelatedField(slug_field='name', many=True,queryset=Product_category.objects.all())


    class Meta:
        model = Product
        fields = ['id', 'name', 'default_price', 'description', 'deleted','product_category']

