from django.contrib import admin
from .models import OODBeispiel


class BspAdmin(admin.ModelAdmin):
    pass
admin.site.register(OODBeispiel, BspAdmin)
