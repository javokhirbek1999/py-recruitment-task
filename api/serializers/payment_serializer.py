from rest_framework import serializers



class PaymentSerializer(serializers.Serializer):
    """Serialzier for payment"""

    transaction_id = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    currency = serializers.CharField(required=True)
