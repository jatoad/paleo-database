from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Specimen
from .forms import CommentForm, SpecimenForm


class SpecimenList(generic.ListView):
    model = Specimen
    queryset = Specimen.objects.filter(status=1).order_by("-upload_date")
    template_name = "index.html"


class SpecimenInfo(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Specimen.objects.filter(status=1)
        specimen = get_object_or_404(queryset, slug=slug)
        comments = specimen.comments.filter(approved=True).order_by(
            "-created_on"
            )

        return render(
            request,
            "specimen_page.html",
            {
                "specimen": specimen,
                "comments": comments,
                "comment_form": CommentForm(),
                "specimen_form": SpecimenForm(),
            }
        )
