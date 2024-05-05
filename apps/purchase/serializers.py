from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['url','po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date']
