from rest_framework import serializers

from apps.sponsors.api_endpoints.serializers import SponsorsSerializer
from apps.sponsors.models import Sponsors
from apps.students.models import Students


class StudentsSerializer(serializers.ModelSerializer):
    student_get_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Students
        fields = "__all__"





