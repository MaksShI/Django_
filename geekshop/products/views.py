from django.shortcuts import render

def index(request):
    context = {
        'title': 'магазин',

    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'продукты',
        'price': '2585.9'
    }
    return render(request, 'products/products.html',context)




