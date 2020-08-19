from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns =[
    path('', mainapp.IndexView.as_view(), name='index'),

    path('contact/', mainapp.ContactView.as_view(), name='contact'),

    re_path(r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/$',
            mainapp.category_products, name='category_products'),

    re_path(r'^category/(?P<cpk>\d+)/subcategory/(?P<scpk>\d+)/products/(?P<page>\d+)/$',
            mainapp.category_products, name='category_products_pagination'),
    # path('', mainapp.price_filter),
    # path('higher/<int:h_price>/', mainapp.price_filter),
]
