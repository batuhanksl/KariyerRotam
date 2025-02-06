from django.urls import path
from . import views



urlpatterns = [
    path('', views.MeslekSorgulamaAnaSayfa),
    path('meslekler/<slug:meslek>', views.MeslekSorgulamaByCategory)
]