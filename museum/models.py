from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Specimen(models.Model):
    latin_name = models.CharField(max_length=200, default='latin name')
    english_name = models.CharField(max_length=200, default='name')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='specimen_upload',
        default=True
    )
    specimen_image = CloudinaryField('image', default='placeholder')
    when_found = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200)
    additional_information = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    ordering = ['-upload_date']


def __str__(self):
    return self.species_name
    # self.fields['specimen_image'].required = True


class Comment(models.Model):
    specimen = models.ForeignKey(
        Specimen,
        on_delete=models.CASCADE,
        related_name='Comment'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


class Meta:
    ordering = ['-created_on']


def __str__(self):
    return f"{self.name} commented: {self.comment_content}"
