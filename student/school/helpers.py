from rest_framework import serializers
from .models import Student

def student_view_validate(request_obj):
    # validate as required
    # if True:return True, None 
    # if False:return False, "message"
    if request_obj is not None:
        return {"success": True, "message": "User Validated Successfully"}
    else:
        return {"success": False, "message": "Invalid!"} 

    
def student_view_helper(queryset):
    # all the funtional operations
    ls = list(queryset)
    for i in ls:
        if i.age < 15:
            print('Age is Mixed so showing only > 15')
            return Student.objects.filter(age__gte = 15)
    else:
        print('Age is not less than 15')
        return Student.objects.all()

