from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from mainapp.models import Product, ProductCategory, ProductSubCategory


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


def category_products(request, pk, spk):
    category_list = ProductCategory.objects.all()


    if pk == '0':
        category = {'pk': 0, 'name': 'All categories'}
        subcategory = {'spk': 0, 'name': 'All subcategories'}
        products = Product.objects.filter(is_active=True)

    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        subcategory = get_object_or_404(ProductSubCategory, pk=spk)
        products = subcategory.products.filter(is_active=True)

    context = {
        'page_title': 'Catalog',
        'category_list': category_list,
        'category': category,
        'products': products,
    }
    return render(request, 'mainapp/category.html', context)
