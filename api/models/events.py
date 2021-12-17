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
            'section_rows': self.building.sections_rows,
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
        return self.building.building_info

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
            'building': self.venue.building_info,
            'street': self.venue.street,
            'city': self.venue.city,
            'post_code': self.venue.post_code
        }
    
    def __str__(self) -> str:
        return f"{self.name} | {self.event_date} | {self.venue_info['building']}"