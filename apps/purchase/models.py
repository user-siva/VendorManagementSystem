from django.db import models
from apps.vendors.models import Vendor
from django.core.validators import MinLengthValidator,MaxLengthValidator

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('completed','Completed'),
        ('canceled','Canceled')
    ]
    po_number = models.CharField(max_length=50,unique=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='purchase_orders')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    quality_rating = models.FloatField(null=True,blank=True,validators=[MinLengthValidator(0),MaxLengthValidator(5)])
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}-{self.po_number}"
    