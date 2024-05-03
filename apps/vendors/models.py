from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20,unique=True)
    on_time_delivery_rate = models.FloatField(default=0,validators=[MinLengthValidator(0),MaxLengthValidator(100)])
    quality_rating_avg = models.FloatField(default=0,validators=[MinLengthValidator(0),MaxLengthValidator(5)])
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0,validators=[MinLengthValidator(0),MaxLengthValidator(100)])

    def __str__(self):
        return self.name

class HistoricalPerformance(models.Model):
    Vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='historical_performance')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0,validators=[MinLengthValidator(0),MaxLengthValidator(100)])
    quality_rating_avg = models.FloatField(default=0,validators=[MinLengthValidator(0),MaxLengthValidator(5)])
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0,validators=[MinLengthValidator(0),MaxLengthValidator(100)])

    def __str__(self):
        return f"{self.name}-{self.date}"


