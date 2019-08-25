from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def main(request):
    context = {
        'title': 'Interior'
    }
    return render(request, 'index.html', context=context)

def products(request):
    context = {
        'title': 'Products',
    }
    return render(request, 'products.html', context=context)


def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'contact.html', context=context)