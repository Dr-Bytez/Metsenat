from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.sponsors.api_endpoints.permissions import IsOwnerOrReadOnly
from apps.sponsors.api_endpoints.serializers import SponsorsSerializer
from apps.sponsors.models import Sponsors


class CreateSponsorAPIView(CreateAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer


class ListSponsors(ListAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'sponsorship_amount', 'created_at', ]
    permission_classes = [IsAuthenticated]


class SponsorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
