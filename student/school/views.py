from django.shortcuts import render, get_object_or_404
from .models import Student, Standard, Subject, Teacher
from .serializers import StandardSerialiser, SubjectSerialiser, StudentSerialiser, TeacherSerialiser
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .helpers import student_view_helper, student_view_validate

# Create your views here.
# class StudentViews(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = StudentSerialiser
#     queryset = Student.objects.all()
#     lookup_field = 'id'

#     def get(self, request, id):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)

# class StudentViews(viewsets.ModelViewSet):
#     serializer_class = StudentSerialiser
#     queryset = Student.objects.all()

class StudentViews(viewsets.ViewSet):
    def get(self, request):
        # validation
        success, message = student_view_validate(request)
        if not success:
            return {"success":success, "message":message}
            
        # functional operations
        queryset = Student.objects.all()
        required_response_list = student_view_helper(queryset)

        # serialize the queryset
        required_response_list = StudentSerialiser(required_response_list, many=True)
        return Response({"success":success, "data":required_response_list.data})

    def create(self, request):
        serializer = StudentSerialiser(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        contact = get_object_or_404(queryset, pk = pk)
        serializer = StudentSerialiser(contact)
        return Response(serializer.data)

    def update(self, request, pk=None):
        contact = Student.objects.get(pk=pk)
        serializer = StudentSerialiser(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
