from rest_framework.viewsets import ModelViewSet

from ..models.transaction import Transaction
from ..serializers.transaction_serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    """API View for Transactions"""

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


    