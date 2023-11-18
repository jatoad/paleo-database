from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Specimen(models.Model):
    latin_name = models.CharField(max_length=200, unique=True)
    english_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="museum_posts"
    )
    specimen_image = CloudinaryField('image', default='placeholder')
    additional_information = models.TextField()
    when_found = models.DateTimeField()
    location = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='museumpost_like', blank=True)


    class Meta:
        ordering = ["-upload_date"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
