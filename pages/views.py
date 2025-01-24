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
    return render(request, 'anasayfa.html')


def hakkimizda(request):
    return render(request, 'hakkimizda.html', {'hakkimizdaDB': hakkimizdaDB})