from django.shortcuts import render
from django.http import HttpResponse


hakkimizdaDB = {
    "insanlar" : [ 
        {
            "ad":"Batuhan KIŞLACI",
            "mail":"info@batuhankislaci.com",
            "imageURL":"https://media.licdn.com/dms/image/v2/C4D03AQGzFirVs04WTQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1607013701338?e=1743033600&v=beta&t=7zNN5Hbkj2N7Qp4lU6x9ELOCGlUXzsp_oORBrIgxv3w"
        },
        {
            "ad":"Hanife YILDIZHAN",
            "mail":"hnfyldzhn@gmail.com",
            "imageURL":"https://media.licdn.com/dms/image/v2/D4D03AQHAg-9JZzl3QQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1697309644894?e=1743033600&v=beta&t=Di-X_5TiuvLB_bX0eKJEV-IQEag-1L69UmF8hzutdGc"
        },
        {
            "ad":"Rasim Fatih ZENGİN",
            "mail":"fzengin2015@gmail.com",
            "imageURL":"https://media.licdn.com/dms/image/v2/C4D03AQH0lOWLQFCaDg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1654504030306?e=1743033600&v=beta&t=CaJyaNnGamBm0kpRr7a4LE_1wrsnWbypWUWLzCLxAyg"
        }
    ],
    "infoParagraph" : "Bu proje, Eskişehir Teknik Üniversitesi Endüstri Mühendisliği bitirme projesi kapsamında yapılmıştır. Proje, üniversite öğrencileri ve yeni mezunların kariyer süreçlerinde yaşadıkları zorluklara yardımcı olmak amacı ile geliştirilmiştir. Kullanıcılara kariyer planlaması sürecinin her aşamasında yardımcı olmak amaçlanmaktadır.",
}



def home(request):
    pages = [
        {
            "header": "Sana en uygun işi bul!",
            "description": "Üniversite öğrencisi, yeni mezun veya yeni kariyer fırsatları arayan birisi misin? Günümüzde senin gibi milyonlarca insan kariyer seçimlerinden memnun değil. Bu yolda mevcut yeteneklerin ile en iyi yapabileceğin işi bulmana yardımcı oluyoruz. Hemen Dene!",
            "link": "/ats/meslekoner/",
        },
        {
            "header": "Özgeçmişini yapay zeka sistemleri okuyabiliyor mu?",
            "description": "Günümüzde büyük ölçekli şirketlerin büyük çoğunluğu yoğun başvuruları hızlı bir şekilde elemek için aday takip sistemlerini kullanıyor. Bu ön eleme havuzundan avantajlı çıkmak için özgeçmişinin yapay zeka uygulamaları tarafından okunabilirliğini en yüksek seviyede tutmak gerekmektedir. Peki senin özgeçmişin sana avantaj sağlıyor mu? Hemen test et!",
            "link": "/ats/",
        },
        {
            "header": "Farklı meslekleri keşfet!",
            "description": "Maaş bilgileri, ilgili bölümler, sektörler ve gerekli yetenekler hakkında detaylı verilerle geleceğinizi daha net planlayın. Hemen tıklayın ve birbirinden farklı yüzlerce mesleği keşfedin!",
            "link": "/meslek-sorgulama/",
        },
        {
            "header": "Biz Kimiz?",
            "description": "Bu proje, Eskişehir Teknik Üniversitesi Endüstri Mühendisliği bitirme projesi kapsamında yapılmıştır. Proje, üniversite öğrencileri ve yeni mezunların kariyer süreçlerinde yaşadıkları zorluklara yardımcı olmak amacı ile geliştirilmiştir. Kullanıcılara kariyer planlaması sürecinin her aşamasında yardımcı olmak amaçlanmaktadır.",
            "link": "/hakkimizda/",
        }
    ]
    return render(request, 'anasayfa.html', {'pages': pages})


def hakkimizda(request):
    return render(request, 'hakkimizda.html', {'hakkimizdaDB': hakkimizdaDB})