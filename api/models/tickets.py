from django.db import models
from django.db.models.fields import CharField
from django.db.models.manager import Manager

from api.models.reservation import Reservation

from .events import Event, Seat


AVAILABLE = 'available'
BOOKED = 'booked'
SELECTED = 'selected'

class TicketManger(Manager):
    """Ticket Model Manager"""

    # Query all tickets 
    def all(self):
        return super().all()
    
    # Queries all available tickets
    def available(self):
        return Ticket.objects.filter(status=AVAILABLE)
    
    # Queries all booked tickets
    def booked(self):
        return Ticket.objects.filter(status=BOOKED)
    
    # Queries all selected tickets
    def selected(self):
        return Ticket.objects.filter(status=SELECTED)
    


class Ticket(models.Model):
    """Ticket model"""

    TICKET_STATUSES = (
        (AVAILABLE, 'Available'),
        (BOOKED, 'Booked'),
        (SELECTED, 'Selected')
    )

    EVEN = 'even'
    ALL_TOGETHER = 'all together'
    AVOID_ONE = 'avoid one'

    SELLING_OPTIONS = (
        (EVEN, 'Even'),
        (ALL_TOGETHER, 'All together'),
        (AVOID_ONE, 'Avoid one')
    )
    
    

    ticket_type = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    selling_option = CharField(choices=SELLING_OPTIONS, max_length=100, blank=True, null=True)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=TICKET_STATUSES, max_length=100, default=AVAILABLE) 
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)

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
    
    @property
    def details(self):
        return {
            'id': self.id,
            'type': self.ticket_type,
            'seat': self.seat_details, 
        }

    objects = TicketManger()

    def __str__(self) -> str:
        return f"Ticket type: {self.ticket_type} | Event: {self.event.__str__()} | [Section: {self.seat_details['section']} | Row: {self.seat_details['row']} | Number: {self.seat_details['seat_number']}] | Status: {self.status}"
