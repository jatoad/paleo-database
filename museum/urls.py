from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.SpecimenList.as_view(), name='home'),
    path('<slug:slug>/', views.SpecimenInfo.as_view(), name='specimen_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)