from django.shortcuts import render
from django.views import generic, View
from .models import Specimen


class SpecimenList(generic.ListView):
    model = Specimen
    queryset = Specimen.objects.filter(status=1).order_by("-upload_date")
    template_name = "index.html"


class SpecimenInfo(View):
    
    def get(self, request, *args, **kwargs):
        queryset = post.objects.filter(status=1)
        specimen = get_object_or_404(queryset)
        comments = post.comments.filter(approved=true).order_by('created_on')

        return render(
            request,
            "specimen.html", 
            {
                "specimen": specimen,
                "comments": comments
            }
        )

    
