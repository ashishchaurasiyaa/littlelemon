from rest_framework import serializers
from .models import MenuItem, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'description', 'price', 'inventory']


class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = '__all__'
