from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(Product)