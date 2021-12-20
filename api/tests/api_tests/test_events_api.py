from datetime import datetime, timedelta
from django.urls import reverse

from django.test import TestCase


from rest_framework.test import APIClient

from api.models.events import Building, Event, TicketSet, Venue


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

def create_ticket_sets(ticket_type, selling_option, quantity, price, event):
    """
    Helper function to create set of tickets.
    Once the TicketSet model sends post_save signal, 
    Ticket model instances will be created for specified event 
    in a specified quantity by a specified ticket type, selling option and price 
    """

    TicketSet.objects.create(ticket_type=ticket_type, selling_option=selling_option, quantity=quantity, price=price, event=event)
    

EVENTS = reverse('events:all-list')
BUILDINGS = reverse('events:buildings-list')
VENUES = reverse('events:venues-list')
class TestEventsAPIs(TestCase):

    def setUp(self):
        self.client = APIClient
        self.building = create_building(name='One World Land', sections=3, section_rows=4 ,rows=3)
        self.venue = create_venue(building=self.building, street='University Street', city='London', post_code='LSOW 987')
        self.event = create_event(
            name='One World Music Festival', 
            description='This is description', 
            event_date=datetime(year=2022, month=4, day=22),
            door_opens_at=datetime(year=2022, month=4, day=22, hour=15, minute=0, second=0).time(), 
            start_time=datetime(year=2022, month=4, day=22, hour=16, minute=0, second=0).time(),
            end_time=datetime(year=2022, month=4, day=22, hour=17, minute=0, second=0).time(),
            venue=self.venue)
    