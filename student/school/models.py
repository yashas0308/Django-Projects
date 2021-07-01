from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
# student model -->name(str), marks, age, roll_no, class(Foreign Key)
# teacher model -->name, subject(Foreign Key), age
# subject model --> name
# standard model --> class(str), subjects(many to many), class_teacher (Foreign Key) 

class Subject(models.Model):
    name = models.CharField(max_length=50)

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    age = models.IntegerField()

class Standard(models.Model):
    classes = models.CharField(max_length=1)
    subject = models.ManyToManyField(Subject)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    classes = models.ForeignKey(Standard, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=50)
    marks = models.IntegerField()







