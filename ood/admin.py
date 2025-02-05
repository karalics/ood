from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import OODBeispiel

def send_status_change_email(obj, old_status, new_status):
    # Hole die Anzeigeversionen der Stati
    status_dict = dict(OODBeispiel.STATUS_CHOICES)
    old_status_display = status_dict.get(old_status, old_status)
    new_status_display = status_dict.get(new_status, new_status)
    subject = "Status geaendert"
    message = (
        f"Hallo,\n\n"
        f"Dein Eintrag mit ID {obj.bsp_id} hat den Status gewechselt.\n"
        f"Von: {old_status_display}\n"
        f"Zu: {new_status_display}\n\n"
        "Viele Gruesse,\n"
        "Dein Team"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [obj.kontakt_email])

def set_status_neu(modeladmin, request, queryset):
    for obj in queryset:
        old_status = obj.status
        obj.status = 'neu'
        obj.save()
        send_status_change_email(obj, old_status, 'neu')
set_status_neu.short_description = "Setze Status auf Neu"

def set_status_eingeplant(modeladmin, request, queryset):
    for obj in queryset:
        old_status = obj.status
        obj.status = 'eingeplant'
        obj.save()
        send_status_change_email(obj, old_status, 'eingeplant')
set_status_eingeplant.short_description = "Setze Status auf Eingeplant"

def set_status_in_bearbeitung(modeladmin, request, queryset):
    for obj in queryset:
        old_status = obj.status
        obj.status = 'in_bearbeitung'
        obj.save()
        send_status_change_email(obj, old_status, 'in_bearbeitung')
set_status_in_bearbeitung.short_description = "Setze Status auf In Bearbeitung"

def set_status_abgeschlossen(modeladmin, request, queryset):
    for obj in queryset:
        old_status = obj.status
        obj.status = 'abgeschlossen'
        obj.save()
        send_status_change_email(obj, old_status, 'abgeschlossen')
set_status_abgeschlossen.short_description = "Setze Status auf Abgeschlossen"

class BspAdmin(admin.ModelAdmin):
    list_display = ('bsp_id', 'beispielsatz', 'status', 'kontakt_email')
    actions = [set_status_neu, set_status_eingeplant, set_status_in_bearbeitung, set_status_abgeschlossen]

admin.site.register(OODBeispiel, BspAdmin)
