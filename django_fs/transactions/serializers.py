from rest_framework import serializers

from .models import UserTransactions


class UserTransactionsSerializer(serializers.ModelSerializer):
    operation_dt = serializers.DateTimeField(read_only=True)
    change_dt = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserTransactions
        fields = ["user", "amount", "operation_dt", "change_dt", "kind", "category"]
