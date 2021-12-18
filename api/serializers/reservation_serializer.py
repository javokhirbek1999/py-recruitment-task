from django.utils.translation import gettext as _

from rest_framework import serializers

from ..models.reservation import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    """Serializer for Reservation Model"""

    class Meta:
        model = Reservation
        fields = ('id', 'ticket', 'member', 'reservation_option', 'date_created', 'expiry_time', 'quantity', 'total_price', 'status')
    

    def validate(self, attrs):
        """Validate reservation"""

        EVEN = 'even'
        ALL_TOGETHER = 'all together'
        AVOID_ONE = 'avoid one'

        reservation_option = attrs['reservation_option']
        quantity = attrs['quantity']
        
        if reservation_option == EVEN:
            if quantity%2!=0:
                msg = _('Please choose even number of tickets')
                raise serializers.ValidationError(msg)
        elif reservation_option == ALL_TOGETHER:
            pass
            

