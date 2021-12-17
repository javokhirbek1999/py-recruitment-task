from time import time
from django.db import models
from datetime import datetime, timedelta

from .users import User
from .tickets import Ticket


class Reservation(models.Model):
    """Reservation model"""

    PAID = 'paid'
    NOT_PAID = 'not paid'
    CANCELED = 'canceled'

    RESERVATION_STATUS = (
        (PAID, 'Paid'),
        (NOT_PAID, 'Not paid'),
        (CANCELED, 'Cancelled')
    )

    EVEN = 'even'
    ALL_TOGETHER = 'all together'
    AVOID_ONE = 'avoid one'

    RESERVATION_OPTIONS = (
        (EVEN, 'Even'),
        (ALL_TOGETHER, 'All together'),
        (AVOID_ONE, 'Avoid one')
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=None)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_option = models.CharField(choices=RESERVATION_OPTIONS, max_length=200, default=AVOID_ONE)
    date_created = models.DateTimeField(auto_now_add=True)
    expiry_time = models.DateTimeField(default=datetime.now()+timedelta(minutes=15))
    quantity = models.IntegerField(default=1) # Read Only
    total_price = models.IntegerField(default=0)
    status = models.CharField(choices=RESERVATION_STATUS, max_length=200, default=NOT_PAID)


    def __str__(self) -> str:
        return f'Ticket: {self.ticket} | Event: {self.ticket.event.name} | Reservation Option: {self.reservation_option}'

