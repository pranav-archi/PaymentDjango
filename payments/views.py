from django.shortcuts import render
from django.conf import settings
import razorpay
# Create your views here.
def home(request):
    return render(request,'payments/payments.html')

def create_order(request):
    print("CREATE ORDER VIEW CALLED")
    client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    amount = 10000

    order = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'receipt': 'receipt_001'
    })
    print("ORDER:", order)
    return render(request,'payments/payments.html',{'order': order,'razorpay_key_id': settings.RAZORPAY_KEY_ID})