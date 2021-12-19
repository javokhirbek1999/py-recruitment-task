from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models.tickets import Ticket

from ..serializers.reservation_serializer import ReservationSerializer
from ..serializers.payment_serializer import PaymentSerializer
from ..models.reservation import Reservation
from ..permissions.reservation_permissions import IsReservationOwner

from api.utils import payment 


class ReservationViewSet(ModelViewSet):
    """API View for Reservation Model"""

    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    """Detail API View for Reservation Model"""

    permission_classes = (IsReservationOwner, )
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().get(event__id=kwargs.get('event_id'), client__id=kwargs.get('client_id'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
    

class ReservationPaymentView(RetrieveUpdateDestroyAPIView):
    """API View for Reservation Payment"""

    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().get(event__id=kwargs.get('event_id'), client__id=kwargs.get('client_id'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_queryset().get(event__id=kwargs.get('event_id'), client_id=kwargs.get('client_id'))

        

        for ticket in Ticket.objects.filter(reservation=instance):
            ticket.status = 'booked'
            ticket.save()
        instance.status = 'paid'
        instance.save()

        return Response({'message': 'success'})




