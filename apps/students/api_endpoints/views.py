from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.sponsors.api_endpoints.permissions import IsOwnerOrReadOnly
from apps.students.api_endpoints.serializers import StudentsSerializer
from apps.students.models import Students




class StudentCreateAPIView(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]


class ListStudentsAPIView(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_filelds = ['student_level_type', 'university_name', ]


class StudentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
