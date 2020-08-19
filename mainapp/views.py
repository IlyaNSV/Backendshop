from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from mainapp.models import Product, ProductCategory, ProductSubCategory, ProductBrand


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


def category_products(request, cpk, scpk, page=1, l_price=None):
    category_list = ProductCategory.objects.all()
    brands_list = ProductBrand.objects.all()
    on_page = 1
    range = [1, 2, 3]
    if cpk == '0':
        category = {'pk': 0, 'name': 'All categories'}
        subcategory = {'pk': 0, 'name': 'All subcategories'}
        products = Product.objects.filter(is_active=True)


    else:
        category = get_object_or_404(ProductCategory, pk=cpk)
        subcategory = get_object_or_404(ProductSubCategory, pk=scpk)
        products = subcategory.sc_products.filter(is_active=True)

    products_paginator = Paginator(products, on_page)
    try:
        products = products_paginator.page(page)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        'page_title': 'Catalog',
        'category_list': category_list,
        'brands_list': brands_list,
        'category': category,
        'subcategory': subcategory,
        'products': products,
        'range': range,
    }

    return render(request, 'mainapp/category.html', context)

