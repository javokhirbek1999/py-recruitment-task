from django.views import generic
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models.transaction import Transaction
from ..serializers.transaction_serializers import TransactionSerializer
# from ..serializers.payment_serializer import PaymentSerializer


class TransactionViewSet(ModelViewSet):
    """API View for Transactions"""

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'messsage': 'Transaction completed. Thank you'}, status=status.HTTP_200_OK)
        
        return Response({'message': 'Error occurred while processing your payment. Detail: {}'.format(serializer.errors)},status=status.HTTP_400_BAD_REQUEST)


# class PaymentApiView(generics.CreateAPIView):
#     """API View for processing payment"""

#     serializer_class = PaymentSerializer
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             return Response({'data':serializer.data})