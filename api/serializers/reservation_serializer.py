from django.utils.translation import gettext as _

from rest_framework import serializers

from api.models.tickets import Ticket

from ..models.reservation import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    """Serializer for Reservation Model"""

    class Meta:
        model = Reservation
        fields = ('id', 'client', 'client_details', 'event', 'event_details', 'date_created', 'expiry_time', 'quantity', 'total_price', 'status')
        extra_kwargs = {
            'client': {'write_only': True},
            'client_details': {'read_only': True},
            'event': {'write_only': True},
            'event_details': {'read_only': True},
            'date_created': {'read_only': True,},
            'expiry_time': {'read_only': True},
            'total_price': {'read_only': True}
        }

