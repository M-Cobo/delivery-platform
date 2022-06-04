from dataclasses import fields
from pyexpat import model
from turtle import distance
from rest_framework import serializers
from django.contrib.auth.models import User
from stores.models import Store

class NearbyStoreSerializer(serializers.Serializer):
    distance = serializers.SerializerMethodField()

    def get_distance(self, instance):
        return instance.distance.mi if instance else 'N/A'

    class Meta:
        model = Store
        fields = [
            'id', 'name', 'rating', 'opening_hour', 'closing_hour', 'store_type',
            'address', 'latitude', 'longitude', 'distance',
        ]