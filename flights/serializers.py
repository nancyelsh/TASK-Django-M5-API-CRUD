from rest_framework import serializers

from .models import Booking, Flight


class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "price", "time", "destination"]


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "date", "flight"]

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "flight", "date", "passengers"]