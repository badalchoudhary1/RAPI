from django.urls import path
from .views import StudentView, StudentListView, StudentViewbyID

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),  # List all students
    path('students/<int:id>/', StudentViewbyID.as_view(), name='student-detail'),  # View, update or delete specific student
    path('students/create/', StudentView.as_view(), name='student-create'),  # Create a new student
]