from django.db import models

from api.models.reservation import Reservation


class Transaction(models.Model):
    """Transaction Model"""

    GBP = 'GBP'
    OTHER = 'OTHER'

    CURRENCY_OPTIONS = (
        (GBP, 'GBP'),
        (OTHER, 'OTHER')
    )

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)    
    currency = models.CharField(choices=CURRENCY_OPTIONS, max_length=100, default=GBP)
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

    def __str__(self) -> str:
        return f"Reservation: {self.reservation}"

