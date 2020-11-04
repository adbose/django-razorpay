from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .config import TEST_KEY_ID, TEST_KEY_SECRET

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = 10000  # paise

        client = razorpay.Client(
            auth=(TEST_KEY_ID, TEST_KEY_SECRET)
        )
        payment = client.order.create(
            {
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'
            }
        )
    return render(request, "index.html")


@csrf_exempt
def success(request):
    return render(request, "success.html")
