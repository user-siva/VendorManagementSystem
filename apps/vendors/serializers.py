from rest_framework import serializers
from .models import Vendor,HistoricalPerformance
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ['pk','name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

class HistoricalPerformanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = ['pk','Vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'username']
        extra_kwargs = {'password': {'write_only':True, 'min_length':5}}


    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password('password', None)
            user.save()

        return user

class AuthTokenserializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request= self.context.get('request'),
            username = email,
            password = password,
        )

        if not user:
            raise serializers.ValidationError('unable to authorize', code='authorization')

        attrs['user'] = user
        return attrs