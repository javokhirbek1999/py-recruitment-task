from rest_framework.serializers import ModelSerializer

from ..models.transaction import Transaction


class TransactionSerializer(ModelSerializer):
    """Serializer for Transaction Model"""

    class Meta:
        model = Transaction
        fields = ('id', 'reservation', 'reservation_details', 'total_amount', 'currency', 'date')
        extra_kwargs = {
            'reservation': {'write_only': True},
        }