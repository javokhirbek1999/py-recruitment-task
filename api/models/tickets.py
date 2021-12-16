from django.db import models

from .events import Event


class Ticket(models.Model):
    """Ticket model"""

    PREMIUM = 'premium'
    GOLD = 'gold'
    STANDARD = 'standard'

    TICKET_TYPES = (
        (PREMIUM,'permium'),
        (GOLD, 'gold'),
        (STANDARD, 'standard')
    )

    ticket_type = models.CharField(choices=TICKET_TYPES, max_length=100, default=STANDARD)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

