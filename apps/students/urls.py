

from django.urls import path

from apps.students.api_endpoints.views import StudentCreateAPIView, ListStudentsAPIView, StudentRetrieveAPIView

urlpatterns = [
    path("create/", StudentCreateAPIView.as_view()),
    path("student/<pk>", StudentRetrieveAPIView.as_view()),
    path("list/", ListStudentsAPIView.as_view()),
]