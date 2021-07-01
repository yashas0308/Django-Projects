from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import serializers, views
from .models import Person
from .forms import PersonForm
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage
from .pagination import CustomPageNumberPagination
from .serialisers import PersonDetailSerialiser, PhoneNumSerialiser
from .helpers import phone_view_helper, phone_view_validate

class ContactList(viewsets.ViewSet, CustomPageNumberPagination):

    queryset = Person.objects.all()
    serializer_class = PersonDetailSerialiser

    def list(self, request):
        queryset = Person.objects.all().order_by('first_name')
        serializer = PersonDetailSerialiser(queryset, many=True)
        self.page_size = 5
        paginated_queryset = self.paginate_queryset(serializer.data, request)
        paginated_response = self.get_paginated_response(paginated_queryset)
        return Response(paginated_response.data)
    
    def retrieve(self, request, pk=None):
        person_obj = Person.objects.get(id=pk)
        serializer = PersonDetailSerialiser(person_obj)
        paginated_queryset  = self.paginate_queryset(serializer.data, request)
        paginated_response = self.get_paginated_response(paginated_queryset)
        return Response(paginated_response.data)

class PhoneNumList(viewsets.ViewSet):

    def get(self , request):
        # validation
        success, message = phone_view_validate(request)
        if not success:
            return {"success":success, "message":message}
        # functional operations
        queryset = Person.objects.filter(id>1)
        required_response_list = phone_view_helper(queryset)
        # serialize the queryset
        required_response_list = PhoneNumSerialiser(required_response_list)
        #response
        return Response({"success":success, "data":required_response_list})        

def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    
    p = Paginator(persons, 5)
    
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {
        'persons': page, 

        'count': persons.count()
        }
    # import pdb; pdb.set_trace()
    return render(request, 'contact/contact_list.html', context)


def contact_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'contact/contact_detail.html', {'person': person})


def contact_new(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PersonForm()
    return render(request, 'contact/contact_edit.html', {'form': form})


def contact_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/person/' + str(person.pk))
    else:
        form = PersonForm(instance=person)
    return render(request, 'contact/contact_edit.html', {'form': form})


def contact_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('/')
