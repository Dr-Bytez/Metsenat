from rest_framework import serializers

from apps.sponsors.models import Sponsors


class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = "__all__"
        read_only_fields = ['id', 'created_at']

    #def validate_
