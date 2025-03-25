from django.urls import path
from . import views

app_name = 'KisilikTesti'

urlpatterns = [
    path('', views.sorular),
]