from rest_framework.viewsets import ModelViewSet


from ..serializers import event_serializers
from ..models import events

class EventsViewSet(ModelViewSet):
    """API View for Events"""
    
    serializer_class = event_serializers.EventSerializer
    queryset = events.Event.objects.all()


class BuildingsViewSet(ModelViewSet):
    """API View for Buildings"""

    serializer_class = event_serializers.BuildingSerializer
    queryset = events.Building.objects.all()


class SeatViewSet(ModelViewSet):
    """API View for Seats"""

    serializer_class = event_serializers.SeatSerializer
    queryset = events.Seat.objects.all()


class VenueViewSet(ModelViewSet):
    """API View for Venue"""

    serializer_class = event_serializers.VenueSerializer
    queryset = events.Venue.objects.all()