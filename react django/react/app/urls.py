from django.urls import path
from .views import student_list_create_update_delete

urlpatterns = [
    path('students/', student_list_create_update_delete, name='student-list-create'),
    path('students/<int:pk>/', student_list_create_update_delete, name='student-detail'),
]
 