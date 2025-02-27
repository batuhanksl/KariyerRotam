from django.urls import path
from . import views

app_name = 'MeslekSorgulama'

urlpatterns = [
    path('', views.MeslekSorgulamaAnaSayfa),
    path('meslekler/<slug:meslek>', views.MeslekSorgulamaByCategory, name="meslek_sorgulama")
]