from rest_framework import viewsets
from .serializers import PurchaseOrderSerializer
from .models import PurchaseOrder
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import generics

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
    def partial_update(self,request,*args,**kwargs):
        instance = self.get_object()

        instance.acknowledgment_date = timezone.now()
        instance.save(update_fields=['acknowledgment_date'])

        return Response({'details':'Acknowledged Successfully'})
