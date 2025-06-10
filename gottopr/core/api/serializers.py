from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Setting,Job,Recent_jobs,Customer,Service,Contact


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Setting
        fields='__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'


class Recent_jobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recent_jobs
        fields='__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields='__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact 
        fields='__all__'



