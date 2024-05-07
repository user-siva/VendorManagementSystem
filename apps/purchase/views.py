from rest_framework import viewsets
from .serializers import PurchaseOrderSerializer
from .models import PurchaseOrder,Vendor
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import generics,status

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    
class AcknowledgePurchaseOrderView(generics.RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'
    
    def partial_update(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()
        instance.save(update_fields=['acknowledgment_date'])

        return Response({'details':'Acknowledged Successfully'},status=status.HTTP_200_OK)
    
    def get_serializer(self,*args,**kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args,**kwargs)
