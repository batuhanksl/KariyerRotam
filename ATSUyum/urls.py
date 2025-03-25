from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path("meslekoner/", views.upload_and_process_resume, name="meslekoner")

]
