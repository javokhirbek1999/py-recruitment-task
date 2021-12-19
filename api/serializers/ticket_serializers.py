from rest_framework import serializers


from ..models import tickets


class TicketSerializer(serializers.ModelSerializer):
    """Serializer for Ticket model"""

    class Meta:
        model = tickets.Ticket
        fields = ('id', 'event', 'event_info', 'ticket_type', 'seat', 'price', 'status')
        

class ReserveTicketSerializer(serializers.ModelSerializer):
    """Serializer for Reserving ticket"""

    class Meta:
        model = tickets.Ticket
        fields = ('id', 'event', 'event_info', 'ticket_type', 'seat', 'price', 'status', 'reservation')
        extra_kwargs = {
            'event': {'read_only': True},
            'ticket_type': {'read_only': True},
            'seat': {'read_only': True},
            'price': {'read_only': True},
        }