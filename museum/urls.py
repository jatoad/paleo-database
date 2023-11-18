from . import views
from django.urls import path


urlpatterns = [
    path('', views.SpecimenList.as_view(), name='home'),
    path('<slug:slug>/', views.SpecimenInfo.as_view(), name='specimen_page'),
    path('like/<slug:slug>', views.SpecimenLike.as_view(), name='specimen_like'),
]
