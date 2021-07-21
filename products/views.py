from datetime import datetime

from django.shortcuts import render

# Create your views here.
# контроллеры = views (вьюхи) = функции

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог'
    }
    return render(request, 'products/products.html', context)