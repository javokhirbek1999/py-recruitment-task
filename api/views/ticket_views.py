from datetime import timedelta, datetime

from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from ..serializers.ticket_serializers import TicketSerializer, ReserveTicketSerializer
from ..models.tickets import Ticket
from ..models.reservation import Reservation


class TicketViewSet(ModelViewSet):
    """List API View for Tickets"""
    
    permission_classes = ()
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(event__id=self.kwargs.get('event_id'), ticket_type=self.kwargs.get('ticket_type'), status=self.kwargs.get('status'))

        
class TicketDetailView(RetrieveAPIView):
    """Detail API View for Tickets that gets ticket by seat id"""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().get(event__id=kwargs.get('event_id'),seat__id=kwargs.get('seat_id'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReserveTicketView(RetrieveUpdateAPIView):
    """API View for reserving a selected ticket"""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReserveTicketSerializer
    lookup_field = 'seat_id'
    queryset = Ticket.objects.all()


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().get(event__id=kwargs.get('event_id'),seat__id=kwargs.get('seat_id'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_queryset().get(event__id=kwargs.get('event_id'), seat__id=kwargs.get('seat_id'))

        user = request.user

        if instance.status == 'selected':
            return Response({'message': 'This seat has been selected by another user but has not been booked yet, you can wait until it is realased if user will not buy it. Thank you. You have been put into a queue'}, status=status.HTTP_200_OK)
        if instance.status == 'booked':
            return Response({'message': 'This seat has already been booked. Please choose a different seat'}, status=status.HTTP_200_OK)
        if user.is_authenticated:
            reservation = None
            
            try:
                reservation = Reservation.objects.get(client=user)
            except Reservation.DoesNotExist:
                # If reservation does not exist, create new reservation and set reservation expiry time
                reservation = Reservation.objects.create(client=user, event=instance.event, expiry_time=datetime.now()+timedelta(minutes=15))
            
            # Calculate the total price of the tickets (One use can buy multiple tickets in a sinle reservation)
            reservation.total_price = reservation.total_price+instance.price
            
            # Keep track of the tickets in the reservation
            reservation.quantity = reservation.quantity+1

            # Set the ticket status to select to avoid multiple users buying same ticket
            instance.status = 'selected'
            instance.reservation = reservation

            instance.save()
            reservation.save()

            return Response({'message': f'Ticket {instance.id} for seat {instance.seat_details} has been successfully selected'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized action'}, status=status.HTTP_401_UNAUTHORIZED)





        
