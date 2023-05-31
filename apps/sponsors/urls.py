

from django.urls import path
from apps.sponsors.api_endpoints import views


urlpatterns = [
    path('create/', views.CreateSponsorAPIView.as_view()),
    path("sponsor/<pk>", views.SponsorRetrieveAPIView.as_view()),
    path("list/", views.ListSponsors.as_view()),
]