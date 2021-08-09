from django.urls import path
from product.views import *

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name="product-view"),
    path('products/<int:pk>', ProductGetAPIView.as_view(), name="product-single-view"),
    path('products-edit/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name="products-edit"),
]
