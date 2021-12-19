from django.db import models

from api.models.events import Event

from .users import User


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

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    expiry_time = models.DateTimeField(default=None)
    quantity = models.IntegerField(default=1) # Read Only
    total_price = models.IntegerField(default=0)
    status = models.CharField(choices=RESERVATION_STATUS, max_length=200, default=NOT_PAID)


    @property
    def client_details(self):
        return {
            'id': self.client.id,
            'email': self.client.email,
            'first_name': self.client.first_name,
            'last_name': self.client.last_name
        }
    
    @property
    def event_details(self):
        return {
            'id': self.event.id,
            'name': self.event.name,
            'description': self.event.description,
            'event_date': self.event.event_date,
            'door_opens_at': self.event.door_opens_at,
            'start_time': self.event.start_time,
            'end_time': self.event.end_time,
            'venue': self.event.venue_info
        }


    def __str__(self) -> str:
        return f'Client: {self.client.first_name} {self.client.last_name} | Event: {self.event.name} '
