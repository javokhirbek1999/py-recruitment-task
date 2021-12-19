from rest_framework import serializers

from ..models.reservation import Reservation


class PaymentSerializer(serializers.Serializer):
    """Serialzier for payment"""

    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    currency = serializers.CharField(max_length=50, required=False)
    token = serializers.CharField(required=True)

    # class Meta:
    #     model = Reservation
    #     fields = ('id', 'self', 'amount', 'currency', 'token')
