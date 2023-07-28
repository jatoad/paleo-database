from .models import Comment, Specimen
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SpecimenForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'english_name',
            'latin_name',
            'specimen_image',
            'when_found',
            'location',
            'additional_information',
        )
