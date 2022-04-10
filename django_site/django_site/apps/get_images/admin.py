from django.contrib import admin
from .models import PagesToScan


# Register your models here.
@admin.register(PagesToScan)
class PagesToScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')
