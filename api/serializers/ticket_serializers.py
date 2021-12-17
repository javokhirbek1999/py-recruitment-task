from rest_framework import serializers


from ..models import tickets


class TicketSerializer(serializers.ModelSerializer):
    """Serializer for Ticket model"""

    class Meta:
        model = tickets.Ticket
        fields = ('id', 'event', 'ticket_type', 'quantity', 'price', 'event_info', 'available_tickets')


