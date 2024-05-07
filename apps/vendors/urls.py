from rest_framework import routers
from django.urls import path,include
from .views import VendorViewSet,VendorPerformanceView

router = routers.DefaultRouter()
router.register(r'vendors',VendorViewSet,basename='vendor')

urlpatterns = [
    path('vendors/<int:pk>/performance/',VendorPerformanceView.as_view(),name='vendor-performance'),
    path('',include(router.urls)),
]