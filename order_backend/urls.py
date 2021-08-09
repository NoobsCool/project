from django.contrib import admin
from django.urls import path
import product.urls as product_urls
import agent.urls as agent_urls
import order.urls as order_urls
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += product_urls.urlpatterns
urlpatterns += agent_urls.urlpatterns
urlpatterns += order_urls.urlpatterns
