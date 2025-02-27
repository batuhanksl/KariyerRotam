from django.shortcuts import render
from .models import Meslek,MeslekSektor,MeslekBolum
from django.shortcuts import get_object_or_404


def MeslekSorgulamaAnaSayfa(request):
    return render(request, 'MeslekSorgulamaAnaSayfa.html', {'meslekler': Meslek.objects.all()})

def MeslekSorgulamaByCategory(request, meslek):
    meslek = get_object_or_404(Meslek, slug=meslek)

    content = {
        'meslek': meslek,
        'dusuk_maas': meslek.en_dusuk_maas,
        'ortalama_maas': meslek.ortalama_maas,
        'yuksek_maas': meslek.en_yuksek_maas,
        'katilimci': meslek.ankete_katilan_sayisi,
        'sektorler': MeslekSektor.objects.filter(meslek=meslek),
        'bolumler': MeslekBolum.objects.filter(meslek=meslek),
        'yetenekler': meslek.yetenekler.all()
    }
    return render(request, 'MeslekSorgulamaByCategory.html', {'meslek': content["meslek"],'dusuk_maas': content['dusuk_maas'],'ortalama_maas': content['ortalama_maas'],'yuksek_maas': content['yuksek_maas'],'katilimci': content['katilimci'],'sektorler': content["sektorler"],'bolumler': content["bolumler"], 'yetenekler': content["yetenekler"]})