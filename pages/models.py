from django.db import models

class HakkimizdaPanel(models.Model):
    isim = models.CharField(max_length=100)
    mail = models.EmailField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.isim
    
class HakkimizdaPanelAciklama(models.Model):
    aciklama = models.TextField()

    def __str__(self):
        return self.aciklama
    

class Anasayfa(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.header