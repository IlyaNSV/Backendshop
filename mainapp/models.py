from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name='фото категории', upload_to='category_images', blank=True)

    def count_prods(self):
        number = 0
        for sub in self.subs.all():
            number += sub.products.count()
        return number


class ProductSubCategory(models.Model):
    name = models.CharField(verbose_name='имя подкатегории', max_length=64, unique=True)
    category = models.ForeignKey(ProductCategory, verbose_name='категория продукта', on_delete=models.CASCADE,
                                 related_name='subs')
    description = models.TextField(verbose_name='описание подкатегории', blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name='фото категории', upload_to='category_images', blank=True)

    def count_prods(self):
        return self.products.count()

    def get_subs(pk):
        return ProductSubCategory.objects.filter(category=pk).filter(is_active=True)


class ProductBrand(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name='логотип', upload_to='brands_logo', blank=True)


class Product(models.Model):
    MALE = 'мужской'
    FEMALE = 'женский'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'W'),
    )

    subcategory = models.ForeignKey(ProductSubCategory, verbose_name='подкатегория продукта', on_delete=models.CASCADE,
                                    related_name='products')
    brand = models.ForeignKey(ProductBrand, verbose_name='бренд продукта', on_delete=models.CASCADE,
                              related_name='products')
    name = models.CharField('имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField('краткое описание', max_length=64, blank=True)
    desc = models.TextField('описание товара', blank=True)
    price = models.DecimalField('цена продукта', max_digits=8, decimal_places=2, default=0)
    sale_price = models.DecimalField('цена со скидкой', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=10)
    color = models.CharField('цвет', max_length=32, blank=True)
    is_active = models.BooleanField(default=True)
    gender = models.CharField(verbose_name='пол', max_length=15,
                              choices=GENDER_CHOICES, default=MALE)
