from django.db import models

# Create your models here.

class Segproy (models.Model):
    rastreo = models.CharField(max_length=20, unique=True)
    empresa = models.CharField(max_length=100)
    proyecto = models.CharField(max_length=200)
    estatus = models.CharField(max_length=200)
    avance = models.IntegerField(max_length=3)
    entrega = models.CharField(max_length=20)

    def __str__(self):
        return self.rastreo


