from rest_framework import routers
from django.urls import path,include
from .views import PurchaseViewSet

router = routers.DefaultRouter()
router.register(r'purchase_orders',PurchaseViewSet,basename='purchase_order')

urlpatterns = [
    path('',include(router.urls))
]