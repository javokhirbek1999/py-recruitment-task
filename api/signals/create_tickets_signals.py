from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.events import TicketSet, Seat
from ..models.tickets import Ticket


@receiver(post_save, sender=TicketSet)
def create_tickets_signal(sender, instance, created, **kwargs):
    """Signal to create tickets on post save signal by TicketSet model"""

    # Filter all related seats
    event_building_seats = [seat for seat in Seat.objects.filter(building=instance.event.venue.building, ticket_assigned=False)]
    
    if created:
        for _ in range(instance.quantity):
            seat = event_building_seats.pop()
            Ticket.objects.create(ticket_type=instance.ticket_type, event=instance.event, seat=seat, price=instance.price)
            seat.ticket_assigned = True
            seat.save()