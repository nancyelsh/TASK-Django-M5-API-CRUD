from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer, BookingDetailSerializer, BookingUpdateSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer


class BookingView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return BookingUpdateSerializer
        return BookingDetailSerializer
    


