from django.urls import path
from app import views

urlpatterns = [
    path('phone/', views.PhoneSms.as_view({"post":"phone"})),
    path('smsphone/', views.PhoneSms.as_view({"post":"smsphone"})),
]