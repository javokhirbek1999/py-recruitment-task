from rest_framework.viewsets import ModelViewSet

from ..serializers.ticket_serializers import TicketSerializer
from ..models.tickets import Ticket


class TicketViewSet(ModelViewSet):
    """API View for Tickets"""

    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
