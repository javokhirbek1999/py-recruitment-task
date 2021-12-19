from django.utils.translation import gettext as _

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models.reservation import Reservation
from api.models.tickets import Ticket

from ..models.transaction import Transaction
from ..utils.payment import PaymentError, CardError, CurrencyError, PaymentGateway

class TransactionSerializer(ModelSerializer):
    """Serializer for Transaction Model"""

    class Meta:
        model = Transaction
        fields = ('id', 'reservation', 'reservation_details', 'currency', 'date')
        extra_kwargs = {
            'reservation': {'write_only': True},
        }

    def create(self, validated_data):
        
        reservation_id = validated_data['reservation']
        currency = validated_data['currency']

        reservation = Reservation.objects.get(id=reservation_id.id)
        
        PAYMENT = PaymentGateway()

        try:
            PAYMENT.charge(amount=reservation.total_price, currency=currency, token='dksodksodksod')
        except (CardError, PaymentError, CurrencyError) as error:
            raise serializers.ErrorDetail(_('Payment cannot be processed. Detail: {}'.format(error)))
        
        # Query all tickets that is included in current reservation
        tickets = Ticket.objects.filter(reservation=reservation)
        
        # Change ticket availability status once the payment is successful
        for ticket in tickets:
            ticket.status = 'booked'
            ticket.save()

        # Set reservation status to paid once the payment is successful
        reservation.status = 'paid'
        reservation.save()

        validated_data['reservation'] = reservation

        return Transaction.objects.create(**validated_data)

        
