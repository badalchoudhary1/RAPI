from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404

class StudentView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class StudentListView(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"status": "success", "students": serializer.data}, status=status.HTTP_200_OK)


class StudentViewbyID(APIView):
    def get(self, request, id):
        student = get_object_or_404(Students, id=id)
        serializer = StudentSerializer(student)
        return Response({"status": "success", "student": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        student = get_object_or_404(Students, id=id)
        student.delete()
        return Response({"status": "success", "data": "Record Deleted"}, status=status.HTTP_200_OK)

    def put(self, request, id):
        student = get_object_or_404(Students, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        student = get_object_or_404(Students, id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
