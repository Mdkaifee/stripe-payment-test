import os
import stripe
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse

# Load environment variables from .env
load_dotenv()

# Set Stripe keys from environment
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')

def checkout(request):
    return render(request, 'payment/checkout.html')

def create_checkout_session(request):
    domain_url = 'http://127.0.0.1:8000/'
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success/',
            cancel_url=domain_url,
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Test $1 Product',
                        },
                        'unit_amount': 100,
                    },
                    'quantity': 1,
                }
            ]
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def success(request):
    return render(request, 'payment/success.html')

def stripe_config(request):
    return JsonResponse({'publicKey': PUBLISHABLE_KEY})
