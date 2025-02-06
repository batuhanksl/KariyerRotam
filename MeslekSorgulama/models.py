from django.db import models


class Sektor(models.Model):
    sektor = models.CharField(max_length=100)

    def __str__(self):
        return self.meslek.meslek
    
class Bolum(models.Model):
    bolum = models.CharField(max_length=100)

    def __str__(self):
        return self.meslek.meslek
    
class Yetenek(models.Model):
    yetenek = models.CharField(max_length=100)

    def __str__(self):
        return self.meslek.meslek
    

class Meslek(models.Model):
    meslek_adi = models.CharField(max_length=100)
    en_dusuk_maas = models.IntegerField()
    ortalama_maas = models.IntegerField()
    en_yuksek_maas = models.IntegerField()
    ankete_katilan_sayisi = models.IntegerField()
    Sektor = models.ForeignKey(Sektor, on_delete=models.CASCADE)
    sektor_yuzde = models.IntegerField()
    Bolum = models.ForeignKey(Bolum, on_delete=models.CASCADE)
    bolum_yuzde = models.IntegerField()
    Yetenek = models.ForeignKey(Yetenek, on_delete=models.CASCADE)


    def __str__(self):
        return self.meslek