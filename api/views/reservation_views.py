from rest_framework.viewsets import ModelViewSet

from ..serializers.reservation_serializer import ReservationSerializer
from ..models.reservation import Reservation


class ReservationViewSet(ModelViewSet):
    """API View for Reservation Model"""

    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


