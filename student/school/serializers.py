from rest_framework import fields, serializers
from .models import Subject, Teacher, Standard, Student

class SubjectSerialiser(serializers.ModelSerializer):
    class Meta: 
        model = Subject
        fields = ['name']

class TeacherSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'age']

class StandardSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = ['classes', 'subject', 'class_teacher']

class StudentSerialiser(serializers.ModelSerializer):
    # name = serializers.CharField(max_length = 50)
    # age = serializers.IntegerField()
    # classes = serializers.CharField(max_length=1)
    # roll_no = serializers.CharField(max_length  = 50)
    # marks = serializers.IntegerField()
    class Meta:
        model = Student
        fields = '__all__' 