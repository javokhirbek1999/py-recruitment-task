from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
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

    def get_queryset(self):
        return events.Seat.objects.filter(building__id=self.kwargs.get('building_id'))
    
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(events.Seat.objects.get(id=kwargs.get('seat_id')))
        return Response({'seat':serializer.data}, status=status.HTTP_200_OK)


class VenueViewSet(ModelViewSet):
    """API View for Venue"""

    serializer_class = event_serializers.VenueSerializer
    queryset = events.Venue.objects.all()

    def get_queryset(self):
        return events.Venue.objects.filter(city=self.kwargs.get('city'))
    


class TicketSetView(ModelViewSet):
    """API View for creating tickets for sepecific event"""

    serializer_class = event_serializers.TicketSetSerializer
    queryset = events.TicketSet.objects.all()

class DetailTicketSetView(RetrieveAPIView):
    """API VIew for listing ticket sets for specific event by ticket type"""

    serializer_class = event_serializers.TicketSetSerializer
    queryset = events.TicketSet.objects.all()

    def retrieve(self, request, *args, **kwargs):
        event_id = kwargs.get('event_id')
        ticket_type= kwargs.get('ticket_type')
        instance = self.get_queryset().get(event__id=event_id, ticket_type=ticket_type)
        data = self.get_serializer(instance)
        return Response({
            'data':data.data
        },status=status.HTTP_200_OK)