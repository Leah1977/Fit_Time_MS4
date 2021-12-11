from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('add/', views.add_contact_message, name='add_contact_message'),
]
