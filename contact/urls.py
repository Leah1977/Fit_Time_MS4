from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path(
        'add_contact_message.html', views.add_contact_message,
        name='add_contact_message'),
]