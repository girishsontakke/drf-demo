from rest_framework import serializers
from quize.models import Quize


class QuizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quize
        fields = ["name", "date_created"]
