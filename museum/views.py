from django.shortcuts import render
from django.views import generic
from .models import Specimen, Comment


class SpecimenList(generic.ListView):
    model = Specimen
    queryset = Specimen.objects.filter(status=1).order_by(-created_on)
    template_name = 'index.html '
