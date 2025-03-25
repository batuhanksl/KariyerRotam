from django.shortcuts import render
from .models import HakkimizdaPanel, HakkimizdaPanelAciklama, Anasayfa



def hakkimizda(request):
    hakkimizdaDB = HakkimizdaPanel.objects.all()
    aciklama = HakkimizdaPanelAciklama.objects.first()
    return render(request, 'hakkimizda.html', {'hakkimizdaDB': hakkimizdaDB, 'aciklama': aciklama})

pages = [
        {
            "header": "Sana en uygun işi bul!",
            "description": "Üniversite öğrencisi, yeni mezun veya yeni kariyer fırsatları arayan birisi misin? Günümüzde senin gibi milyonlarca insan kariyer seçimlerinden memnun değil. Bu yolda mevcut yeteneklerin ile en iyi yapabileceğin işi bulmana yardımcı oluyoruz. Hemen Dene!",
            "link": "/ats/meslekoner/",
            "img": "images/LevelUp.png"
        },
        {
            "header": "Özgeçmişini yapay zeka sistemleri okuyabiliyor mu?",
            "description": "Günümüzde büyük ölçekli şirketlerin büyük çoğunluğu yoğun başvuruları hızlı bir şekilde elemek için aday takip sistemlerini kullanıyor. Bu ön eleme havuzundan avantajlı çıkmak için özgeçmişinin yapay zeka uygulamaları tarafından okunabilirliğini en yüksek seviyede tutmak gerekmektedir. Peki senin özgeçmişin sana avantaj sağlıyor mu? Hemen test et!",
            "link": "/ats/",
            "img": "images/ATS.png"
        },
        {
            "header": "Farklı meslekleri keşfet!",
            "description": "Maaş bilgileri, ilgili bölümler, sektörler ve gerekli yetenekler hakkında detaylı verilerle geleceğinizi daha net planlayın. Hemen tıklayın ve birbirinden farklı yüzlerce mesleği keşfedin!",
            "link": "/meslek-sorgulama/",
            "img": "images/JobSearch.png"
        },
        {
            "header": "Biz Kimiz?",
            "description": "Bu proje, Eskişehir Teknik Üniversitesi Endüstri Mühendisliği bitirme projesi kapsamında yapılmıştır. Proje, üniversite öğrencileri ve yeni mezunların kariyer süreçlerinde yaşadıkları zorluklara yardımcı olmak amacı ile geliştirilmiştir. Kullanıcılara kariyer planlaması sürecinin her aşamasında yardımcı olmak amaçlanmaktadır.",
            "link": "/hakkimizda/",
            "img": "images/Hakkimizda.png"
        }
    ]

def home(request):
    pages = Anasayfa.objects.all()
    return render(request, 'anasayfa.html', {'pages': pages})


