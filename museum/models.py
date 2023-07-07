from django.db import models
# from django.contrib.auth.models import user
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Specimen(models.Model):
    species_name = models.CharField(max_length=200)
    specimen_image = CloudinaryField('image', default='placeholder')
    date_found = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    additional_information = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    ordering = ['-upload_date']


def __str__(self):
    return self.species_name




