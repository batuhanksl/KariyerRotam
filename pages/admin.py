from django.contrib import admin
from .models import HakkimizdaPanel, HakkimizdaPanelAciklama, Anasayfa

@admin.register(HakkimizdaPanel)
class HakkimizdaPanelAdmin(admin.ModelAdmin):
    list_display = ("isim", "mail", "img")

@admin.register(HakkimizdaPanelAciklama)
class HakkimizdaPanelAciklamaAdmin(admin.ModelAdmin):
    list_display = ("aciklama",)

@admin.register(Anasayfa)
class AnasayfaAdmin(admin.ModelAdmin):
    list_display = ("header", "description", "link", "img")