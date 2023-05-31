from django.urls import include, path



urlpatterns = [
    path('sponsors/', include("apps.sponsors.urls")),
    path('students/', include("apps.students.urls")),
]