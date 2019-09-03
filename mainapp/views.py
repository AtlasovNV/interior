# Create your views here.
from django.shortcuts import render
from .models import ProductCategory, Product
import datetime



def main(request):
    context = {
        'title': 'Interior'
    }
    products = Product.objects.all()

    return render(request, 'index.html', context=context)

def products(request, pk=None):
    print(pk)
    products = Product.objects.filter(category_id=pk).all
    print(products)
    links_menu = [
    #    {'href': 'products_all', 'name': 'все'},
    #   {'href': 'products_home', 'name': 'дом'},
    #    {'href': 'products_office', 'name': 'офис'},
    #    {'href': 'products_modern', 'name': 'модерн'},
    #    {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'Products',
        'links_menu': links_menu,
        #'same_products': same_products,
    }
    return render(request, 'products.html', context=context)


def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'contact.html', context=context)
def history(request):
    context = {
        'title': 'history'
    }
    return render(request, 'history.html', context=context)

def showroom(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'showroom.html', context=context)