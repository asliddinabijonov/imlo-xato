from django.db import models

class Togrisoz(models.Model):
    soz = models.CharField(max_length=255)

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name_plural = "So'zlar"

class NotogriSoz(models.Model):
    soz = models.CharField(max_length=255)
    togrisoz = models.ForeignKey(Togrisoz, on_delete=models.CASCADE)

    def __str__(self):
        return self.soz
    class Meta:
        verbose_name_plural = "So'zlar"