import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm

# Optional Firebase setup for chat logging
try:
    import firebase_admin
    from firebase_admin import credentials, firestore

    cred_path = settings.FIREBASE_CREDENTIALS
    if os.path.exists(cred_path) and not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    firebase_db = firestore.client()
except Exception:
    firebase_db = None


def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/products.html', {'products': products, 'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message', '').lower()
        if 'hello' in message:
            reply = 'Hi from ChatBot!'
        else:
            reply = "I don't understand."
        if firebase_db:
            try:
                firebase_db.collection('chat_logs').add({'message': message, 'reply': reply})
            except Exception:
                pass
        return JsonResponse({'response': reply})
    return JsonResponse({'response': 'Send a POST request.'})
