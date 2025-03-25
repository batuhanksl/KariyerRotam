from django.db import models
from django.utils.text import slugify

class Sektor(models.Model):
    sektor_adi = models.CharField(max_length=100)

    def __str__(self):
        return self.sektor_adi

class Bolum(models.Model):
    bolum_adi = models.CharField(max_length=100)

    def __str__(self):
        return self.bolum_adi

class Yetenek(models.Model):
    yetenek_adi = models.CharField(max_length=100)

    def __str__(self):
        return self.yetenek_adi

class Meslek(models.Model):
    meslek_adi = models.CharField(max_length=100)
    en_dusuk_maas = models.IntegerField()
    ortalama_maas = models.IntegerField()
    en_yuksek_maas = models.IntegerField()
    ankete_katilan_sayisi = models.IntegerField()

    sektorler = models.ManyToManyField(Sektor, through='MeslekSektor')
    bolumler = models.ManyToManyField(Bolum, through='MeslekBolum')
    yetenekler = models.ManyToManyField(Yetenek, through="MeslekYetenek")

    slug = models.SlugField(default="", null=False, max_length=100,unique=True,db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.meslek_adi)
        super(Meslek, self).save(*args, **kwargs)


    def __str__(self):
        return self.meslek_adi

class MeslekSektor(models.Model):
    meslek = models.ForeignKey(Meslek, on_delete=models.CASCADE)
    sektor = models.ForeignKey(Sektor, on_delete=models.CASCADE)
    yuzde = models.IntegerField()  

    def __str__(self):
        return f"{self.sektor.sektor_adi},{self.yuzde}"

class MeslekBolum(models.Model):
    meslek = models.ForeignKey(Meslek, on_delete=models.CASCADE)
    bolum = models.ForeignKey(Bolum, on_delete=models.CASCADE)
    yuzde = models.IntegerField()  

    def __str__(self):
        return f"{self.bolum.bolum_adi},{self.yuzde}"

class MeslekYetenek(models.Model):
    meslek = models.ForeignKey(Meslek, on_delete=models.CASCADE)
    yetenek = models.ForeignKey(Yetenek, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.meslek.meslek_adi} - {self.yetenek.yetenek_adi}"