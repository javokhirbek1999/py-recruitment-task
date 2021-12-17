from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.events import Building, Seat


@receiver(post_save, sender=Building)
def create_seats(sender, instance, created, **kwargs):
    """Signal to create seats once the Building model instance is created"""


    if created:
        sections = instance.sections
        section_rows = instance.section_rows
        row_seats = instance.row_seats

        for section in range(sections):
            for row in range(section_rows):
                for seat in range(row_seats):
                    Seat.objects.create(section=section, row=row, seat_number=seat, building=instance)

        