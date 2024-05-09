from rest_framework import routers
from django.urls import path,include
from .views import VendorViewSet,VendorPerformanceView,CreateTokenView,CreateUserView
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'vendors',VendorViewSet,basename='vendor')

urlpatterns = [
    path('vendors/<int:pk>/performance/',VendorPerformanceView.as_view(),name='vendor-performance'),
    path('user/create', view=CreateUserView.as_view()),
    path('user/token/', view=CreateTokenView.as_view()),
    path('',include(router.urls)),
]