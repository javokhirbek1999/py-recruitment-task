from django.db import models

from api.models.reservation import Reservation
from api.models.tickets import Ticket


class Payment(models.Model):
    """Payment Model"""

    GBP = 'GBP'
    OTHER = 'OTHER'

    CURRENCY_OPTIONS = (
        (GBP, 'GBP'),
        (OTHER, 'OTHER')
    )

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(choices=CURRENCY_OPTIONS, max_length=100, default=GBP)
    token = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def reservation_details(self):
        return {
            'id': self.reservation.id,
            'client': self.reservation.client_details,
            'event': self.reservation.event_details,
            'date': self.reservation.date_created,
            'expiry_time': self.reservation.expiry_time,
            'quantity': self.reservation.quantity,
            'total_price': self.reservation.total_price,
            'status': self.reservation.status
        }

    @property
    def get_included_ticket_details(self):
        data = {}
        
        tickets = Ticket.objects.filter(reservation=self.reservation)
        
        
        for ticket in tickets:
            data[ticket.id] = ticket.details
        
        return data

    def __str__(self) -> str:
        return f"Reservation: {self.reservation}"

