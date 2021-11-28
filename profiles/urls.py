from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('order_history/order_numbers>', views.order_history, name="order_history"),
]