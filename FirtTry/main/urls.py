from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contacts', views.contacts, name='contacts')
]