from django.db import models

# Create your models here.
from django.db import models


class InvoiceItem(models.Model):
    # invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    full_name = models.CharField(max_length=200)
    email_address = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=100)
    bank_account_number = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=10)
    client_name = models.CharField(max_length=200)
    client_address = models.TextField()
    due_date = models.DateField()
    item_description = models.TextField()
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    other_charges = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.invoice_number
