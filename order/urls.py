from django.urls import path
from order.views import *

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name="orders"),
    path('orders/<int:pk>', OrderGetAPIView.as_view(), name="orders-singleview"),
    path('orders-edit/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view(), name="edit-orders"),
]
