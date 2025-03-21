from django.db import models

class Kisilik(models.Model):
    kategori = models.CharField(max_length=50,primary_key=True)
    alt_sınır = models.IntegerField()
    ust_sınır = models.IntegerField()
    dusuk_aciklama = models.TextField()
    ortalama_aciklama = models.TextField()
    yuksek_aciklama = models.TextField()

    def __str__(self):
        return self.kategori

class Factor(models.IntegerChoices):
    POSITIVE = 1, "Positive"
    NEGATIVE = -1, "Negative"

class Sorular(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    kategori = models.ForeignKey(Kisilik, on_delete=models.CASCADE)
    factor = models.IntegerField(choices=Factor.choices)
    soruEN = models.TextField()
    soruTR = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.id



