from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('', views.home),
    path('hakkimizda/', views.hakkimizda),
    path('admin/', admin.site.urls),
    path('meslek-sorgulama/', include('MeslekSorgulama.urls'))
]