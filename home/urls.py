from django.urls import path
from . import views
from .views import generate_pdf

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('invoice_template/<int:invoice_id>/', views.invoice_template, name='invoice_template'),
    path('invoice/pdf/<int:invoice_id>/', generate_pdf, name='generate_pdf'),

]