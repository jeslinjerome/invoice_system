from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import InvoiceItem
from .forms import InvoiceItemForm

# from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse


# Create your views here.
def home(request):
    query = request.GET.get('q', '')  # Get the search query parameter
    invoice_list = InvoiceItem.objects.all()

    if query:
        invoice_list = invoice_list.filter(
            Q(invoice_number__icontains=query) |
            Q(client_name__icontains=query) |
            Q(amount__icontains=query)
        )
    return render(request, "home/index.html", {'invoice_list': invoice_list})


def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
        return HttpResponseRedirect('/')

    else:
        form = InvoiceItemForm()

    return render(request, 'home/create_invoice.html', {'form': form})


def invoice_template(request, invoice_id):
    invoice = get_object_or_404(InvoiceItem, pk=invoice_id)
    return render(request, 'home/invoice_template.html', {'invoice': invoice})


def generate_pdf(request, invoice_id):
    # Fetch the invoice using the ID
    invoice = InvoiceItem.objects.get(id=invoice_id)

    # Render the invoice to an HTML string
    html_string = render_to_string('home/invoice_template.html', {'invoice': invoice})

    # Convert the HTML string to a PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Create an HTTP response with the PDF file
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice_{}.pdf"'.format(invoice_id)
    return response
