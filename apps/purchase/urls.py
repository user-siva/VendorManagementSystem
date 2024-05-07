from rest_framework import routers
from django.urls import path,include
from .views import PurchaseViewSet

router = routers.DefaultRouter()
router.register(r'purchases',PurchaseViewSet,basename='purchase')

urlpatterns = [
    path('',include(router.urls))
]