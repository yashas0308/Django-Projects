from django.contrib import admin
from .models import Student, Standard, Subject, Teacher

# Register your models here.
admin.site.register(Subject)
admin.site.register(Standard)
admin.site.register(Student)
admin.site.register(Teacher)