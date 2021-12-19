from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..serializers.reservation_serializer import ReservationSerializer
from ..models.reservation import Reservation
from ..permissions.reservation_permissions import IsReservationOwner



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




