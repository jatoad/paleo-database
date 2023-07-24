from django.shortcuts import render
from django.views import generic
from .models import Specimen


class SpecimenList(generic.ListView):
    model = Specimen
    queryset = Specimen.objects.filter(status=1).order_by("-upload_date")
    template_name = "index.html"
