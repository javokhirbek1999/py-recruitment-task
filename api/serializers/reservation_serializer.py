from rest_framework import serializers

from ..models.reservation import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    """Serializer for Reservation Model"""

    class Meta:
        model = Reservation
        fields = ('id', 'ticket', 'member', 'reservation_option', 'date_created', 'expiry_time', 'quantity', 'total_price', 'status')