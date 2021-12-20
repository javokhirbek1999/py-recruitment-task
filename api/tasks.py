from django.utils import timezone

from api.models.reservation import Reservation
from api.models.tickets import Ticket

from celery import shared_task
from celery.utils.log import get_task_logger



logger = get_task_logger(__name__)


@shared_task
def release_expired_reservations():
    """Runs periodically to release expired reservations"""
    expired_reservations = Reservation.objects.filter(expiry_time__lt=timezone.now(), status='not paid')
    total_expired_reservations = expired_reservations.count()

    if expired_reservations:
        for expired_reservation in expired_reservations:
            tickets = Ticket.objects.filter(reservation=expired_reservation)
            for ticket in tickets:
                ticket.status = 'available'
                ticket.save()
            expired_reservation.status = 'cancelled'
        return "Released {} expired reservations".format(total_expired_reservations)
    else:
        return "No expired reservations are found"

