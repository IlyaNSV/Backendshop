from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from mainapp.models import Product, ProductCategory, ProductSubCategory, ProductBrand


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


def category_products(request, **kwargs):
    print(kwargs)
    if 'page' not in kwargs:
        kwargs['page'] = 1

    if not request.is_ajax():
        request.session['min_price'] = 0
        request.session['max_price'] = 999999

    if request.is_ajax():
        print('AJAX')
        if 'l_price' in kwargs:
            request.session['min_price'] = kwargs['l_price']
        elif 'u_price' in kwargs:
            request.session['max_price'] = kwargs['u_price']
        elif 'b_name' in kwargs:
            request.session['brand'] = kwargs['b_name']

    min_price = request.session['min_price']
    max_price = request.session['max_price']

    category_list = ProductCategory.objects.all()
    brands_list = ProductBrand.objects.all()

    on_page = 12
    range = [1, 2, 3]

    if kwargs['cpk'] == '0':
        category = {'pk': 0, 'name': 'All categories'}
        subcategory = {'pk': 0, 'name': 'All subcategories'}
        products = Product.objects.filter(
            Q(is_active=True),
            Q(price__lte=max_price)
            & Q(price__gte=min_price))
        if ('brand' in request.session) & (request.session['brand'] != 'All'):
            products = products.filter(brand__name=request.session['brand'])
        print(products)

    else:
        category = get_object_or_404(ProductCategory, pk=kwargs['cpk'])
        subcategory = get_object_or_404(ProductSubCategory, pk=kwargs['scpk'])
        products = subcategory.sc_products.filter(
            Q(is_active=True),
            Q(price__lte=max_price)
            & Q(price__gte=min_price))
        if request.is_ajax() & ('b_name' in kwargs):
            products = products.filter(brand__name=kwargs['b_name'])
        print(products)

    products_paginator = Paginator(products, on_page)

    try:
        products = products_paginator.page(kwargs['page'])
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

    if request.is_ajax():
        result = render_to_string('mainapp/includes/inc__products_list.html', context)
        return JsonResponse({'result': result})

    return render(request, 'mainapp/category.html', context)
