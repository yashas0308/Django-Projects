from .models import Person
from .serialisers import PhoneNumSerialiser


def phone_view_validate(request_obj):
    # validate as required
    if True:return True, None 
    if False:return False, "message"

def phone_view_helper(queryset):
    # all the funtional operations
    return [i['']+10 for i in queryset]