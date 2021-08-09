from django.urls import path

from agent.views import *

urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name="customers"),
    path('customers/<int:pk>', CustomerGetAPIView.as_view(), name="customers-singleview"),
    path('customers-edit/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view(), name="edit-customers"),
    path('users/', UserListCreateAPIView.as_view(), name="users"),
    path('users/<int:pk>', UserGetAPIView.as_view(), name="users-singleview"),
    path('users-edit/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name="edit-users"),
    path('login',LoginView.as_view(),name="login"),
]
