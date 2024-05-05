from rest_framework import viewsets
from .serializers import PurchaseOrderSerializer
from .models import PurchaseOrder

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
