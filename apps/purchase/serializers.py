from rest_framework import serializers
from .models import PurchaseOrder
from apps.vendors.models import Vendor

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['pk','po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date']
