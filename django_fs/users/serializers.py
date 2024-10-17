from rest_framework import serializers

from .models import ClientUser


class ClientUserSerializer(serializers.ModelSerializer):
    registration_dt = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ClientUser
        fields = ["name", "surname", "email", "registration_dt"]
