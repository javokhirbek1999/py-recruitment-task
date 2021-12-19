from django.utils.translation import gettext as _
from rest_framework import serializers

from api.models.tickets import Ticket

from ..models import events


class EventSerializer(serializers.ModelSerializer):
    """Serializer for Event model"""

    class Meta:
        model = events.Event
        fields = ('id', 'name', 'description', 'event_date', 'door_opens_at', 'start_time', 'end_time', 'venue', 'venue_info')
        extra_kwargs = {
            'venue': {'write_only':True,},
            'venue_info': {'read_only': True}
        }

class BuildingSerializer(serializers.ModelSerializer):
    """Serializer for Building model"""

    class Meta:
        model = events.Building
        fields = ('id', 'name', 'sections', 'section_rows', 'row_seats')


class SeatSerializer(serializers.ModelSerializer):
    """Serializer for Seat model"""

    class Meta:
        model = events.Seat
        fields = ('id', 'section', 'row', 'seat_number', 'status', 'building', 'building_info')
        extra_kwargs = {
            'building': {'write_only': True},
            'building_info': {'read_only': True}
        }

class VenueSerializer(serializers.ModelSerializer):
    """Serializer for Venue model"""

    class Meta:
        model = events.Venue
        fields = ('id', 'building', 'building_details', 'street', 'city', 'post_code')
        extra_kwargs = {
            'building': {'write_only': True},
            'building_info': {'read_only': True}
        }

class TicketSetSerializer(serializers.ModelSerializer):
    """Serializer for Ticket Set model"""

    class Meta:
        model = events.TicketSet
        fields = ('id', 'ticket_type', 'selling_option', 'quantity', 'price', 'available_tickets','event', 'event_details')
        extra_kwargs = {
            'event': {'write_only':True},
            'event_details': {'read_only': True}
        }

    def validate(self, attrs):
        """Validate that the number of even selling option tickets are in even quantity"""

        selling_option = attrs['selling_option']
        quantity = attrs['quantity']

        if selling_option == 'even':
            if quantity%2!=0:
                msg = _('Please, enter an EVEN quantity')
                raise serializers.ValidationError(msg)
        
        return attrs


    