from django.db import models


class Building(models.Model):
    """Building model"""

    name = models.CharField(max_length=200, null=True, blank=True)
    sections = models.IntegerField(default=0)
    section_rows = models.IntegerField(default=0, verbose_name='Rows of per section')
    row_seats = models.IntegerField(default=0, verbose_name='Seats per row')

    def __str__(self) -> str:
        return self.name


class Seat(models.Model):
    """Seat model"""

    BOOKED = 'booked'
    AVAILABLE = 'available'
    SELECTED = 'selected' # selected but not booked yet

    SEAT_STATUS = (
        (BOOKED, 'booked'),
        (AVAILABLE, 'available'),
        (SELECTED, 'selected')
    )

    section = models.IntegerField(blank=True, null=False, default=None)
    row = models.CharField(max_length=50, default=None)
    seat_number = models.IntegerField()
    status = models.CharField(choices=SEAT_STATUS, default=AVAILABLE, max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


    @property
    def building_info(self):
        """Method to get building info"""

        return {
            'id': self.building.id,
            'name': self.building.name,
            'sections': self.building.sections,
            'section_rows': self.building.section_rows,
            'row_seats': self.building.row_seats
        } 

    def __str__(self) -> str:
        return f"Section: {self.section} | Row: {self.row} | Seat Number: {self.seat_number}"


class Venue(models.Model):
    """Venue model"""

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=50)


    @property
    def building_details(self):
        """Method to get details about building"""
        return self.building.name

    def __str__(self) -> str:
        return f'{self.building.name}, {self.street}, {self.post_code}, {self.city}'




class Event(models.Model):
    """Event model"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    door_opens_at = models.TimeField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)


    @property
    def venue_info(self):
        """Method to get info about event venue"""
        
        return {
            'id': self.venue.id,
            'building': self.venue.building_details,
            'street': self.venue.street,
            'city': self.venue.city,
            'post_code': self.venue.post_code
        }
    
    def __str__(self) -> str:
        return f"{self.name} | {self.event_date} | {self.venue_info['building']}"


class TicketSet(models.Model):
    """Ticket set model to create set of different types of tickets for specified event"""

    PREMIUM = 'premium'
    GOLD = 'gold'
    STANDARD = 'standard'

    TICKET_TYPES = (
        (PREMIUM,'permium'),
        (GOLD, 'gold'),
        (STANDARD, 'standard')
    )


    EVEN = 'even'
    ALL_TOGETHER = 'all together'
    AVOID_ONE = 'avoid one'

    SELLING_OPTIONS = (
        (EVEN, 'Even'),
        (ALL_TOGETHER, 'All together'),
        (AVOID_ONE, 'Avoid one')
    )


    ticket_type = models.CharField(choices=TICKET_TYPES, max_length=100, default=STANDARD)
    selling_option = models.CharField(choices=SELLING_OPTIONS, max_length=100, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    @property
    def available_tickets(self):
        """Method to get total number of tickets"""

        data = {
            'premium': TicketSet.objects.filter(ticket_type=self.PREMIUM).count(),
            'gold': TicketSet.objects.filter(ticket_type=self.GOLD).count(),
            'standard': TicketSet.objects.filter(ticket_type=self.STANDARD).count()
        }
        return {
            'available_tickets': data['premium']+data['gold_tickets']+data['standard'],
            'detail': data           
        }
    
    @property
    def event_details(self):
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
        return f'Ticket type: {self.ticket_type} | Quantity: {self.quantity} | Price: {self.price} | Event: {self.event.name}'