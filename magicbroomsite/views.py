from django.shortcuts import render, redirect
from django.views.generic import View
from . forms import RequestQuotationForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def home_page(request):
    """
    Displays homepage
    """
    return render(request, "base3.html")

def SuccessSubmission(request):
    """
    Displays Success Page after submissoin

    """
    return render(request, "magicbroom/quote-submitted-success.html")

def TermsOfService(request):
    """
    Displays Terms of Service
    """
    return render(request, "magicbroom/terms-of-service.html")

def PrivacyPolicy(request):
    """
    Displays Privacy Policy
    """
    return render(request, "magicbroom/privacy-policy.html")

# def request_quotation(request):
#     """
#     Displays the quotation request form
#     """
#     return render(request, "magicbroom/request_quotation.html")

# Create class based view to load quotation form
class RequestQuotation(View):

    """
    Displays quotation form
    """
    # Load the form
    def get(self, request):
        context = {
            'form': RequestQuotationForm
        }
        return render(request, "magicbroom/request_quotation.html", context)

    # Method to save form data
    def post(self, request):
        # Bind the form
        form = RequestQuotationForm(request.POST)
        if form.is_valid():
            form.save()
            # form = RequestQuotationForm()
            # messages.success(request, 'Form submission successful')
            subject, from_email, to = 'Quotation Request', 'noreply@magicbroom.us', 'info@magicbroom.us'
            text_content = 'Hello, You have received a quotation request.  Please login to view details'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative('', 'test/html')
            msg.send()
            return redirect('success_submission')
        context = {
            'form': form
        }
        # messages.success(request, 'Errors')
        return render(request, "magicbroom/request_quotation.html", context)
