from .models import Vendor,HistoricalPerformance
from .serializers import VendorSerializer,HistoricalPerformanceSerializer
from rest_framework import generics,viewsets


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
