from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer, BookingDetailSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"

