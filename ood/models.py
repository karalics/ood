from django.db import models

class OODBeispiel(models.Model):
    STATUS_CHOICES = [
        ('neu', 'Neu'),
        ('eingeplant', 'Eingeplant'),
        ('in_bearbeitung', 'In Bearbeitung'),
        ('abgeschlossen', 'Abgeschlossen'),
    ]

    beispielsatz = models.CharField("Beispiel Satz", max_length=300)
    bsp_id = models.AutoField(primary_key=True)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='neu')
    kontakt_email = models.EmailField("Kontakt Email", max_length=254)

    def __str__(self):
        return f"{self.bsp_id}: {self.beispielsatz} ({self.get_status_display()}) - {self.kontakt_email}"
