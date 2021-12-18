from django.db import models

from .events import Event, Seat


class Ticket(models.Model):
    """Ticket model"""

    ticket_type = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True) 


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
    
    @property
    def seat_details(self):
        """Method to get seat details"""

        return {
            'id': self.seat.id,
            'section': self.seat.section,
            'row': self.seat.row,
            'seat_number': self.seat.seat_number,
            'status': self.seat.status,
            'building': self.seat.building_info
        }

    def __str__(self) -> str:
        return f"Ticket type: {self.ticket_type} | Event: {self.event.__str__()}"
