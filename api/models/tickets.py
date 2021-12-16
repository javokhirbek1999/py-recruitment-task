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
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


    @property
    def available_tickets(self):
        """Method to get total number of tickets"""
        data = {
            'premium': Ticket.objects.filter(ticket_type=self.PREMIUM).count(),
            'gold': Event.objects.filter(ticket_type=self.GOLD).count(),
            'standard': Event.objects.filter(ticket_type=self.STANDARD).count()
        }
        return {
            'total_tickets': Ticket.objects.all().count(),
            'available_tickets': data['premium']+data['gold_tickets']+data['standard'],
            'detail': data           
        }
    
    @property
    def event_info(self):
        """Method to get event details"""

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
        return f"{self.ticket_type} | Quantity: {self.quantity} | Event: {self.event.__str__()}"