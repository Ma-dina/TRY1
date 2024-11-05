from rest_framework import serializers
from .models import Inf


class InfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inf
        fields = ["id", "title", "content", "created"]
