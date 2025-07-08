from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm


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
        return JsonResponse({'response': reply})
    return JsonResponse({'response': 'Send a POST request.'})
