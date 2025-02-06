from django.contrib import admin
from .models import Meslek, Sektor, Bolum, Yetenek, MeslekSektor, MeslekBolum, MeslekYetenek


class MeslekSektorInline(admin.TabularInline):  # Alternatif olarak StackedInline kullanılabilir
    model = MeslekSektor
    extra = 1  # Yeni giriş için boş bir alan bırakır


class MeslekBolumInline(admin.TabularInline):
    model = MeslekBolum
    extra = 1

class MeslekYetenekInline(admin.TabularInline):
    model = MeslekYetenek
    extra = 1


@admin.register(Meslek)
class MeslekAdmin(admin.ModelAdmin):
    list_display = ("meslek_adi", "ortalama_maas", "ankete_katilan_sayisi")
    inlines = [MeslekSektorInline, MeslekBolumInline,MeslekYetenekInline]  # Inline'ları admin paneline ekle


@admin.register(Sektor)
class SektorAdmin(admin.ModelAdmin):
    list_display = ("sektor_adi",)


@admin.register(Bolum)
class BolumAdmin(admin.ModelAdmin):
    list_display = ("bolum_adi",)


@admin.register(Yetenek)
class YetenekAdmin(admin.ModelAdmin):
    list_display = ("yetenek_adi",)