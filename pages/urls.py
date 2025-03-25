from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('hakkimizda/', views.hakkimizda),
    path('admin/', admin.site.urls),
    path('meslek-sorgulama/', include('MeslekSorgulama.urls')),
    path('ats/', include('ATSUyum.urls')),
    path('kisilik-testi/', include('KisilikTesti.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)