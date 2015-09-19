from django.shortcuts import render, redirect
from django.views.generic import View
from .payment import payment
from .forms import SendMoneyForm

# # Create your views here.
class IndexView(View):
    def get(self, request):
        form = SendMoneyForm()
        return render(request, 'paypal_app/index.html', {'form': form})
    def post(self, request):
        recipient_email = request.POST['recipient_email']
        dollars = request.POST['dollars']
        # Get the paypal redirect address from payment.py:
        redirect_address = payment(recipient_email, dollars)
        return redirect(redirect_address)

class SuccessView(View):
    def get(self, request):
        return render(request, 'paypal_app/success.html')

class CancelView(View):
    def get(self, request):
        return render(request, 'paypal_app/cancel.html')
