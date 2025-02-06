from django.contrib import admin
from .models import Meslek

# Register your models here.
@admin.register(Meslek)
class MeslekAdmin(admin.ModelAdmin):
    list_display = ('meslek_adi', 'ortalama_maas', 'ankete_katilan_sayisi',)
    search_fields = ('meslek_adi',)
    pass