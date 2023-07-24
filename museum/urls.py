from . import views
from django.urls import path  


# urlpatterns = [
#     path('', views.SpecimenList.as_view(), name='home'),      
# ]

urlpatterns = [
    path('', views.SpecimenList.as_view(), name='home'),
    path(
        '<slug:slug>/',
        views.SpecimenInfo.as_view(),
        name='specimen_details'
    ),
]