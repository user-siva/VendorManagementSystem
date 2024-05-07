from rest_framework import routers
from django.urls import path,include
from .views import PurchaseViewSet,AcknowledgePurchaseOrderView

router = routers.DefaultRouter()
router.register(r'purchase_orders',PurchaseViewSet,basename='purchase_order')

urlpatterns = [
    path('purchase_orders/<str:po_number>/acknowledge/',AcknowledgePurchaseOrderView.as_view(),name='acknowledge-purchase-order'),
    path('',include(router.urls))
]