from rest_framework import serializers
from .models import SayHello


class SayHelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = SayHello
        fields = "__all__"
