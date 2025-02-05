from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.template.response import TemplateResponse
from .models import OODBeispiel

def change_status_with_confirmation(modeladmin, request, queryset, new_status):
    new_status_display = dict(OODBeispiel.STATUS_CHOICES)[new_status]
    # Ermittele das App-Label aus dem ersten Objekt in der Queryset
    app_label = queryset.first()._meta.app_label if queryset.exists() else ''
    # Wenn das Formular bestaetigt wurde
    if request.POST.get('confirm'):
        email_body = request.POST.get('email_body')
        status_dict = dict(OODBeispiel.STATUS_CHOICES)
        for obj in queryset:
            old_status = obj.status
            obj.status = new_status
            obj.save()
            # Ersetze Platzhalter im Mailinhalt:
            final_message = email_body.replace("{{ old_status }}", status_dict.get(old_status, old_status))
            final_message = final_message.replace("{{ new_status }}", new_status_display)
            final_message = final_message.replace("{{ id }}", str(obj.bsp_id))
            send_mail(
                subject="Status geaendert",
                message=final_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[obj.kontakt_email]
            )
        modeladmin.message_user(request, f"Status wurde auf {new_status_display} gesetzt und E-Mails wurden versendet.")
        return None
    else:
        default_message = (
            "Hallo,\n\n"
            "Dein Eintrag mit ID {{ id }} hat den Status gewechselt.\n"
            "Von: {{ old_status }}\n"
            f"Zu: {new_status_display}\n\n"
            "Viele Gruesse,\n"
            "Dein Team"
        )
        context = {
            'queryset': queryset,
            'email_body': default_message,
            'new_status': new_status,
            'action': request.POST.get('action'),
            'app_label': app_label,
        }
        return TemplateResponse(request, "admin/confirm_email_action.html", context)


def set_status_neu(modeladmin, request, queryset):
    return change_status_with_confirmation(modeladmin, request, queryset, 'neu')
set_status_neu.short_description = "Setze Status auf Neu"

def set_status_eingeplant(modeladmin, request, queryset):
    return change_status_with_confirmation(modeladmin, request, queryset, 'eingeplant')
set_status_eingeplant.short_description = "Setze Status auf Eingeplant"

def set_status_in_bearbeitung(modeladmin, request, queryset):
    return change_status_with_confirmation(modeladmin, request, queryset, 'in_bearbeitung')
set_status_in_bearbeitung.short_description = "Setze Status auf In Bearbeitung"

def set_status_abgeschlossen(modeladmin, request, queryset):
    return change_status_with_confirmation(modeladmin, request, queryset, 'abgeschlossen')
set_status_abgeschlossen.short_description = "Setze Status auf Abgeschlossen"

class BspAdmin(admin.ModelAdmin):
    list_display = ('bsp_id', 'beispielsatz', 'status', 'kontakt_email')
    actions = [
        set_status_neu,
        set_status_eingeplant,
        set_status_in_bearbeitung,
        set_status_abgeschlossen
    ]

admin.site.register(OODBeispiel, BspAdmin)
