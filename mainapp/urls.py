from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns =[
    path('', mainapp.IndexView.as_view(), name='index'),
    path('contact/', mainapp.ContactView.as_view(), name='contact'),
    re_path(r'^category/(?P<pk>\d+)/subcategory/(?P<spk>\d+)/products/$',
            mainapp.category_products, name='category_products'),
]
