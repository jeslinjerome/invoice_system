from django.contrib import admin
from .models import InvoiceItem


# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'full_name', 'bank_name', 'client_name')


admin.site.register(InvoiceItem, DataAdmin)
