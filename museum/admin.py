from django.contrib import admin
from .models import Specimen, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Specimen)
class SpecimenAdmin(SummernoteModelAdmin):

    summernote_fields = ('additional_information')


@admin.register(Comment)
class CommentsAdmin(SummernoteModelAdmin):

    summernote_fields = ('comment_content')
