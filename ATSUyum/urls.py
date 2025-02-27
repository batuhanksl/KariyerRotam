from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path("meslekoner/", views.upload_resume_oneri, name="meslekoner"),
    path('ozgecmis/<int:resume_id>', views.ozgecmis, name='ozgecmis')

]
