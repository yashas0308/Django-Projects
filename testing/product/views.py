from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404
from .models import Product
from .forms import ProductForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializers, UserSerializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
# @permission_classes((IsAuthenticated))
def registration_view(request):

    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class ProductModelViewSets(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

def home(request):
    return render(request, 'home.html', {})

def about(request):
    my_content = {
        "name": "this is about me YASH",
        "about": "Hi I'm a Software Developer",
        "phone": 9879876565,
        "education": "B.E in CSE ",
        "college": "East West institute of Technology",
        "marks" : [83.34, 86.67, 75, "6.71CGPA"]
    }
    return render(request, 'about.html', my_content)

def contact(request):
    return render(request, 'contact.html', {})


def product_create_detail(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, "product/prod_create.html", context)

def dynamic_loookup_url(request, my_id):
    try:
        obj  = Product.objects.get(id = my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object" : obj
    }
    return render(request, "product/detail.html", context)


def product_view_detail(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'Name' : obj.name,
    #     'Description' : obj.desc
    # }
    context = {
        'object' : obj
    }
    return render(request, "product/detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "product/prod_delete.html", context)

def product_list_view(request):

    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset,
    }
    return render(request, "product/prod_list.html", context)

def register_user(request):
    return render(request, "product/register.html")



