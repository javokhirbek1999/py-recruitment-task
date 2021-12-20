from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from rest_framework import serializers

from api.models.tickets import Ticket

from ..models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Serialzier for payment"""

    class Meta:
        model = Payment
        fields = ('id','amount','currency','token','date','reservation','reservation_details','get_included_ticket_details')
        extra_fields = {
            'reservation': {
                'write_only': True,
            },
            'amount': {'required': False,}, 
        }
    

    def validate(self, attrs):
        """Validation for ticket types (Even, All-together, Avoid-one)"""

        reservation = attrs['reservation']


        tickets = Ticket.objects.filter(reservation=reservation)

        EVEN = 'even'
        ALL_TOGETHER = 'all together'
        AVOID_ONE = 'avoid one'

        even_type_tickets = tickets.filter(selling_option=EVEN)
        all_together_type_tickets = tickets.filter(selling_option=ALL_TOGETHER)
        avoid_one_type_tickets = tickets.filter(selling_option=AVOID_ONE)

        if even_type_tickets.count()>0:
            if even_type_tickets.count()%2!=0:
                msg = _('You can buy only EVEN number of tickets, please select select EVEN number of tickets')
                raise ValidationError(msg)
        
        if all_together_type_tickets.count()>0:
            
            previous_seat = None

            for ticket in all_together_type_tickets:
                if previous_seat is None:
                    previous_seat = ticket.id
                else:
                    if ticket.seat.id+1 != previous_seat.id and ticket.seat.section != previous_seat.section and ticket.seat.row != previous_seat.row:
                        msg = _('Please select seats that are next to each other')
                        raise ValidationError(msg)
                    previous_seat= ticket.seat
        
        if avoid_one_type_tickets.count()>0:
            if tickets.filter(status='available').count()==1:
                msg = _('Please do not leave only 1 ticket available, consider including that 1 available ticket in your reservation too')
                raise ValidationError(msg)
        
        reservation.save()

        attrs['reservation'] = reservation

        return attrs
    



        
        