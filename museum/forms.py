from .models import Comment, Specimen
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SpecimenForm(forms.ModelForm)

