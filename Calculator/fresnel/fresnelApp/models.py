from django.db import models

# Create your models here.

class Datos(models.Model):
    km = models.FloatField(max_length=20, blank=True, null=True)
    Ghz = models.FloatField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.km