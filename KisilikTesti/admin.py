from django.contrib import admin
from .models import Sorular, Kisilik
from django.utils.html import format_html

@admin.register(Sorular)
class SorularAdmin(admin.ModelAdmin):
    list_display = ("id", "kategori", "factor", "soruEN", "soruTR")


@admin.register(Kisilik)
class KisilikAdmin(admin.ModelAdmin):
    list_display = ("kategori", "alt_sinir", "ust_sinir","custom_description", "dusuk_aciklama", "ortalama_aciklama", "yuksek_aciklama")

    def custom_description(self, obj):
        return format_html("<i>Kullanıcının alabildiği en düşük skor 10 en yüksek skor 50'dir. Lütfen bu aralıklarda veriyi 3'e bölünüz.</i>")  # You can replace this with any HTML or plain text

    custom_description.short_description = 'Description'  