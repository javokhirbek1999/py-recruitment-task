from django.test import TestCase

from ...models.events import Building, Venue, Event


def create_building(name, sections, section_rows, rows):
    """Helper function to create Building model instance"""
    
    building = Building.objects.create(name=name, sections=sections, section_rows=section_rows, row_seats=rows)
    return building

def create_venue(building, street, city, post_code):
    """Helper function to create Venue model instance"""

    venue = Venue.objects.create(building=building, street=street, city=city, post_code=post_code)
    return venue

def create_event(name, description, event_date, door_opens_at, start_time, end_time, venue):
    """Helper function to create Event model instance"""

    event = Event.objects.create(name=name, description=description, event_date=event_date, door_opens_at=door_opens_at, start_time=start_time, end_time=event_date, venue=venue)
    return event


class TicketsModelTests(TestCase):
    """Tests for Tickets Moddel"""

    
    