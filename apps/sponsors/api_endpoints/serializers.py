from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.sponsors.models import Sponsors


class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = "__all__"
        read_only_fields = ['id', 'created_at', ]

    def validate(self, attrs):
        print(attrs['company_name'])
        print(attrs['sponsor_type'])
        if 'individual' in attrs['sponsor_type'] and attrs['company_name']:
            raise ValidationError("Don't write company name for entity")

        return attrs


