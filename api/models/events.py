from django.db import models


class Building(models.Model):
    """Building model"""

    name = models.CharField(max_length=200, null=True, blank=True)
    sections = models.IntegerField(default=0, verbose_name='You can leave it blank')
    section_rows = models.IntegerField(default=0, verbose_name='Total number of rows of seats per section')
    row_seats = models.IntegerField(default=0, verbose_name='Total number of seats per row')


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

    section = models.IntegerField(blank=True, null=False)
    row = models.CharField(max_length=50)
    seat_number = models.IntegerField()
    status = models.CharField(choices=SEAT_STATUS, default=AVAILABLE, max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"Section: {self.section} | Row: {self.row} | Seat Number: {self.seat_number}"


class Venue(models.Model):
    """Venue model"""

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=50)


    def __str__(self) -> str:
        return f'{self.building.name}, {self.street}, {self.post_code}, {self.city}'


class Event(models.Model):
    """Event model"""
    name = models.CharField(max_length=200)
    premium_tickets = models.IntegerField(default=0)
    gold_tickets = models.IntegerField(default=0)
    standard = models.IntegerField(default=0)
    total_tickets = models.IntegerField(default=0) # Read Only
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    door_opens_at = models.TimeField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)


    @property
    def available_tickets(self):
        """Method to get total number of tickets"""
        data = {
            'premium': Event.objects.filter(premium_tickets__gte=1).count(),
            'gold': Event.objects.filter(gold_tickets__gte=1).count(),
            'standard': Event.objects.filter(standard__gte=1).count()
        }
        return {
            'available_tickets': data['premium']+data['gold_tickets']+data['standard'],
            'detail': data           
        }


    @property
    def venue_info(self):
        """Method to get info about event venue"""
        
        return {
            'name': self.venue.name,
            'building': self.venue.building,
            'street': self.venue.street,
            'city': self.venue.city,
            'post_code': self.venue.post_code
        }