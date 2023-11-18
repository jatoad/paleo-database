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
        queryset = Specimen.objects.filter(status=0)
        specimen = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if specimen.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "specimen_page.html",
            {
                "specimen": specimen,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Specimen.objects.filter(status=0)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.specimen = specimen
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "specimen_page.html",
            {
                "specimen": specimen,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

class SpecimenLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        specimen = get_object_or_404(Specimen, slug=slug)
        if specimen.likes.filter(id=request.user.id).exists():
            specimen.likes.remove(request.user)
        else:
            specimen.likes.add(request.user)

        return HttpResponseRedirect(reverse('specimen_like', args=[slug]))

