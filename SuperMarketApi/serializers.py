from django.db.models import fields
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length = 100)
    subcategory = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()
    class Meta:
        model = Item
        fields = ('name','category','subcategory','amount')
        
class ItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"