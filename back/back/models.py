from django.db import models

class Etalon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class EtalonProperty(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    etalon = models.ForeignKey(Etalon, related_name='etalon_properties', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    