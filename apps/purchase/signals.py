from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import PurchaseOrder

@receiver(post_save,sender=PurchaseOrder)
def update_performance_metrics(sender,instance,**kwargs):
    vendor = instance.vendor
    

    #on_time_delivery_rate
    completed_orders = vendor.purchase_orders.filter(status='completed')
    on_time_deliveries = completed_orders.filter(delivery_date__lte=models.F('delivery_date'))
    completed_orders_count = completed_orders.count()
    if completed_orders_count>0:
        vendor.on_time_delivery_rate = (on_time_deliveries.count()) / completed_orders_count * 100
    else:
        vendor.on_time_delivery_rate = 0
    

    #quality rating average
    completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
    if completed_orders_with_rating.exists():
        avg_rating = completed_orders_with_rating.aggregate(avg_rating=models.Avg('quality_rating'))['avg_rating']
        if avg_rating is not None:
            vendor.quality_rating_avg = avg_rating
    
    #average response time
    print("acknowledged")
    acknowledge_orders = vendor.purchase_orders.exclude(acknowledgment_date__isnull=True)
    print("acknowledge_orders:",acknowledge_orders)
    if acknowledge_orders.exists():
        print("ackowledged")
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() for order in acknowledge_orders]
        print("response_times:",response_times)
        vendor.average_response_time = sum(response_times) / len(response_times)

    #fullfillment rate
    vendor.fulfillment_rate = (completed_orders.filter(status='completed').count() / vendor.purchase_orders.count()) * 100

    vendor.save()
