from rest_framework import serializers

from ..models import events


class EventSerializer(serializers.ModelSerializer):
    """Serializer for Event model"""

    class Meta:
        model = events.Event
        fields = ('id', 'name', 'description', 'event_date', 'door_opens_at', 'start_time', 'end_time', 'venue_info')


class BuildingSerializer(serializers.ModelSerializer):
    """Serializer for Building model"""

    class Meta:
        model = events.Building
        fields = ('id', 'name', 'sections', 'section_rows', 'row_seats')


class SeatSerializer(serializers.ModelSerializer):
    """Serializer for Seat model"""

    class Meta:
        model = events.Seat
        fields = ('id', 'section', 'row', 'seat_number', 'status', 'building_info')


class VenueSerializer(serializers.ModelSerializer):
    """Serializer for Venue model"""

    class Meta:
        model = events.Venue
        fields = ('id', 'building_details', 'street', 'city', 'post_code')