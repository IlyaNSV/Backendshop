from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.IndexView.as_view(), name='index'),

    path('contact/', mainapp.ContactView.as_view(), name='contact'),

    re_path(r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/$',
            mainapp.category_products, name='category_products'),

    re_path(r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/(?P<page>\d+)/$',
            mainapp.category_products, name='category_products_pagination'),

    # PRODUCTS FILTERS PATHS
    re_path(r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/filter/price/lower/(?P<l_price>\d+)/$',
            mainapp.category_products),

    re_path(r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/filter/price/upper/(?P<u_price>\d+)/$',
            mainapp.category_products),

    re_path(
        r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/(?P<page>\d+)/'
        r'filter/price/lower/(?P<l_price>\d+)/$',
        mainapp.category_products),

    re_path(
        r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/(?P<page>\d+)/'
        r'filter/price/upper/(?P<u_price>\d+)/$',
        mainapp.category_products),

    re_path(r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/filter/brand/(?P<b_name>.+\w+)/$',
            mainapp.category_products),

    re_path(
        r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/(?P<page>\d+)/'
        r'filter/brand/(?P<b_name>.+\w+)/$',
        mainapp.category_products),
    # path('', mainapp.price_higher_filter),
]
