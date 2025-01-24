from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

meslekler = ["bilgisayar","endüstri"]

yetenekler = ["C#","Python","C++","Ruby"]

def MeslekSorgulamaAnaSayfa(request):
    return render(request, 'MeslekSorgulamaAnaSayfa.html')

def MeslekSorgulamaByCategory(request, meslek):
    if meslek not in meslekler:
        return HttpResponse("<h1>404</h1>")
    return render(request, 'MeslekSorgulamaByCategory.html', {'meslek': meslek, 'yetenekler': yetenekler})