from django.contrib import admin
from .models import Specimen, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Specimen)
class SpecimenAdmin(SummernoteModelAdmin):

    summernote_fields = ('additional_information')
    list_filter = ('species_name', 'location', 'when_found', 'author', 'upload_date')
    list_display = ('species_name', 'upload_date',)
    search_fields = ['species_name', 'location', 'author']


@admin.register(Comment)
class CommentsAdmin(SummernoteModelAdmin):

    summernote_fields = ('comment_content')
    list_display = ('name', 'comment_content', 'specimen', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
