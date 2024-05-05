from rest_framework import serializers
from .models import Vendor,HistoricalPerformance

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ['url','name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

class HistoricalPerformanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = ['url','Vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']