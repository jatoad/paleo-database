from . import views
from django.urls import path  


urlpatterns = [
    path('', views.SpecimenList.as_view(), name='home'),      
]
