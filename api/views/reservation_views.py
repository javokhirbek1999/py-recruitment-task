from django.core.exceptions import RequestAborted
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models.tickets import Ticket

from api.utils.payment import CardError, CurrencyError, PaymentError, PaymentGateway

from ..serializers.reservation_serializer import ReservationSerializer
from ..serializers.payment_serializer import PaymentSerializer

from ..models.reservation import Reservation
from ..models.payment import Payment

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
        instance = self.get_queryset().get(id=kwargs.get('reservation_id'))
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
    



class PaymentApiView(ModelViewSet):
    """API View for processing payments"""

    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    
    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated], url_path='pay')
    def pay(self, request, pk=None):
        """Payment processing endpoint"""

        serializer = PaymentSerializer(data=request.data)

        reservation = Reservation.objects.get(id=pk)
        
        if serializer.is_valid():
            
            data = serializer.data

            amount = data.get('amount')
            token = data.get('token')
            currency = data.get('currency')

            PAYMENT = PaymentGateway()
            amount = float(amount)
            # Validate the total amount being paid by the user
            if amount!=reservation.total_price:
                if amount < reservation.total_price:
                    return Response({'error': 'You are required to pay {} {}. Current amount tried to pay {} {}'.format(reservation.total_price, currency, amount, currency)}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # If user pays more than required payment, charge only required amount of payment
                    # 
                    # Example: Required amount to pay: 1200
                    #          User's entered amount:  1500
                    #          Amount to return to user: 1500 - 1200 = 300
                    #          In this case , user tried to pay 300 more GBP 
                    amount = amount - (amount - float(reservation.total_price))
            try:
                result = PAYMENT.charge(amount=reservation.total_price, currency=currency, token=token)
            except (CardError, PaymentError, CurrencyError) as error:
                return Response({'message': 'failed', 'detail': error}, status=status.HTTP_400_BAD_REQUEST)

            # Query all tickets that are included in current reservation
            tickets = Ticket.objects.filter(reservation=reservation)

            # Change ticket availability status to 'booked once the payment is successful
            for ticket in tickets:
                ticket.status = 'booked'
                ticket.save()
            
            # Set reservation status to paid once the payment is successful
            reservation.status = 'paid'
            reservation.save()

            Payment.objects.create(reservation=reservation, amount=amount, currency=currency, token=token)

            return Response({'message': 'Payment for {} has been successfully processed'.format(reservation), 'payment_details': result, 'details':data}, status=status.HTTP_200_OK)

        return Response({'message': 'Your payment cannot be processed. Details: {}'.format(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=True, url_path='transactions')
    def transactions(self, request, pk=None):
        payments = None
        try:
            payments = Payment.objects.filter(reservation__event__id=pk)
        except Payment.DoesNotExist:
            return Response({'status':'failed', 'message': 'No payment history for selected event'})
        
        serializer = self.get_serializer(payments, many=True)
        return Response({'status': 'success','payments': serializer.data}, status=status.HTTP_200_OK)
        
        
