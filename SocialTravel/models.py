from django.db import models

class Post(models.Model):
    carousel_caption_title = models.CharField(max_length=30)
    carousel_caption_description = models.CharField(max_length=80)
    heading = models.CharField(max_length=15)
    description = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} - {self.heading}"



class Futbol(models.Model):
    Equipo = models.CharField(max_length=30)
    Ganados = models.CharField(max_length=80)
    Empatados = models.CharField(max_length=15)
    Perdidos = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} - {self.Ganados}"