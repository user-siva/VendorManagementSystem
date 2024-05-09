from .models import Vendor,HistoricalPerformance
from .serializers import VendorSerializer,HistoricalPerformanceSerializer,UserSerializer,AuthTokenserializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def retrieve(self,request,*args,**kwargs):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate':vendor.on_time_delivery_rate,
            'quality_rating_avg':vendor.quality_rating_avg,
            'average_response_time':vendor.average_response_time,
            'fulfillment_rate':vendor.fulfillment_rate,
        }

        return Response(performance_data)
    
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer 
    permission_classes = [AllowAny] 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        print("data:",{
            'user': serializer.data,
            'token': token.key
        })
        return Response({
            'user': serializer.data,
            'token': token.key
        }, status=201)

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenserializer
    permission_classes = [AllowAny] 

    