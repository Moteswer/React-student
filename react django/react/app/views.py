from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_list_create_update_delete(request, pk=None):
    """
    List all students, create a new student, update an existing student, or delete a student.
    """
    if request.method == 'GET':
        if pk:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(student)
        else:
            students = Student.objects.all().order_by('name')
            serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if not pk:
            return Response({'error': 'Method PUT is not allowed without an ID'}, status=status.HTTP_400_BAD_REQUEST)
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not pk:
            return Response({'error': 'Method DELETE is not allowed without an ID'}, status=status.HTTP_400_BAD_REQUEST)
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

