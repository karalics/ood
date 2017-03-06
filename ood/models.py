from django.db import models
from . import settings


class OODBeispiel(models.Model):
    beispielsatz = models.CharField("Beispiel Satz", max_length=300)
    bsp_id = models.AutoField(primary_key=True)

