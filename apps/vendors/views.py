from .models import Vendor,HistoricalPerformance
from .serializers import VendorSerializer,HistoricalPerformanceSerializer
from rest_framework.response import Response
from rest_framework import generics,viewsets


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
   

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    
    def retrieve(self,request,*args,**kwargs):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate':vendor.on_time_delivery_rate,
            'quality_rating_avg':vendor.quality_rating_avg,
            'average_response_time':vendor.average_response_time,
            'fulfillment_rate':vendor.fulfillment_rate,
        }

        return Response(performance_data)
    