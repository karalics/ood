from django.contrib import admin
from .models import OODBeispiel

def set_status_neu(modeladmin, request, queryset):
    queryset.update(status='neu')
set_status_neu.short_description = "Setze Status auf Neu"

def set_status_eingeplant(modeladmin, request, queryset):
    queryset.update(status='eingeplant')
set_status_eingeplant.short_description = "Setze Status auf Eingeplant"

def set_status_in_bearbeitung(modeladmin, request, queryset):
    queryset.update(status='in_bearbeitung')
set_status_in_bearbeitung.short_description = "Setze Status auf In Bearbeitung"

def set_status_abgeschlossen(modeladmin, request, queryset):
    queryset.update(status='abgeschlossen')
set_status_abgeschlossen.short_description = "Setze Status auf Abgeschlossen"

class BspAdmin(admin.ModelAdmin):
    list_display = ('bsp_id', 'beispielsatz', 'status')
    actions = [set_status_neu, set_status_eingeplant, set_status_in_bearbeitung, set_status_abgeschlossen]

admin.site.register(OODBeispiel, BspAdmin)

