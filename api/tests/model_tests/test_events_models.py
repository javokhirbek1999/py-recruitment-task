from datetime import datetime, time
from django.test import TestCase


from ...models.events import Event, Building, Seat, Venue


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

class EventsModelTests(TestCase):
    """Tests for Event Model"""

    def setUp(self):
        self.building = create_building(name='Spodek Arena', sections=3, section_rows=5, rows=8)
        self.venue = create_venue(building=self.building, street='Wojciecha Korfantego', city='Katowice', post_code='40-005')
        self.event = create_event(name='IEM Katowice 2022', description='CS:GO IEM Katowice 2022 at Spodek Arena', event_date=datetime(2022,2,25), door_opens_at=time(17,0,0), start_time=time(18,0,0), end_time=time(20,0,0), venue=self.venue)

    def test_create_seats_successful_on_buidling_instance_created(self):
        """Test signal to create seats on post save signal from Building model"""
        
        total_seats = Seat.objects.all().count()

        self.assertGreater(total_seats,0)
        self.assertEqual(total_seats, self.building.sections*self.building.section_rows*self.building.row_seats)
    
    def test_event_venue_is_set_correctly(self):
        """Test assigning venue building and event venue is successful"""

        self.assertEqual(self.venue.building, self.building)
        self.assertEqual(self.event.venue, self.venue)

    

