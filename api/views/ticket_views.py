from datetime import timedelta, datetime

from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.decorators import action

from ..serializers.ticket_serializers import TicketSerializer, ReserveTicketSerializer
from ..models.tickets import Ticket
from ..models.reservation import Reservation



class AllTicketsViewSet(ModelViewSet):
    """List all tickets for all available events"""

    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    @action(detail=True, url_path='available')
    def available_tickets(self, request, pk=None):
        available_tickets = Ticket.objects.available().filter(event__id=pk)
        serializer = self.get_serializer(available_tickets, many=True)
        return Response({'quantity':available_tickets.count(), 'tickets':serializer.data}, status=status.HTTP_200_OK)
    

    @action(detail=True, url_path='booked')
    def booked(self, request, pk=None):
        booked_tickets = Ticket.objects.filter(status='booked').filter(event__id=pk)
        serializer = self.get_serializer(booked_tickets, many=True)
        return Response({'quantity':booked_tickets.count(), 'tickets': serializer.data}, status=status.HTTP_200_OK)

    
    @action(detail=True, url_path='selected')
    def selected(self, request, pk=None):
        selected_tickets = Ticket.objects.selected().filter(event__id=pk)
        serializer = self.get_serializer(selected_tickets, many=True)
        return Response({'quantity': selected_tickets.count(), 'tickets': serializer.data}, status=status.HTTP_200_OK)


class TicketViewSet(ModelViewSet):
    """List Ticket API View for Specific Event"""
    
    # permission_classes = ()
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
        instance = None
        try:
            instance = self.get_queryset().get(event__id=kwargs.get('event_id'),id=kwargs.get('ticket_id'))
        except Ticket.DoesNotExist:
            return Response({'error': 'The ticket you are looking for does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReserveTicketView(RetrieveUpdateAPIView):
    """API View for reserving a selected ticket"""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReserveTicketSerializer
    lookup_field = 'seat_id'
    queryset = Ticket.objects.all()


    def retrieve(self, request, *args, **kwargs):
        print(kwargs)
        instance = None
        try:
            instance = self.get_queryset().get(event__id=kwargs.get('event_id'),id=kwargs.get('ticket_id'))
        except Ticket.DoesNotExist:
            return Response({'error': 'Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        instance = None
        try:
            instance = self.get_queryset().get(event__id=kwargs.get('event_id'),id=kwargs.get('ticket_id'))
        except Ticket.DoesNotExist:
            return Response({'error':'Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        user = request.user

        if instance.status == 'selected':
            return Response({'message': 'This seat has been selected by another user but has not been booked yet, you can wait until it is realased if user will not buy it. Thank you. You have been put into a queue'}, status=status.HTTP_200_OK)
        if instance.status == 'booked':
            return Response({'message': 'This seat has already been booked. Please choose a different seat'}, status=status.HTTP_200_OK)
        if user.is_authenticated:
            reservation = None
            
            try:
                reservation = Reservation.objects.get(client=user, status='not paid')

                if reservation.status == 'paid':
                    raise Reservation.DoesNotExist # If current client already made a different reservation, then create a new reservation
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





        
