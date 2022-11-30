from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100, db_index=True)
    slug = models.SlugField('Имя ссылки на категорию', max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField('Название товара', max_length=150, db_index=True)
    slug = models.CharField('Название товара в адресе', max_length=150, db_index=True, unique=True)
    image = models.ImageField('Фотография', upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField('Описание товара', max_length=1000, blank=True)
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=0)
    available = models.BooleanField('Наличие', default=True)
    created = models.DateTimeField('Дата создания товара', auto_now_add=True)
    uploaded = models.DateTimeField('Дата обновления товара', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])




class Data(models.Model):
    tele = models.CharField('Телефон', max_length=20)
    gmail = models.CharField('Почта', max_length=50)
    FIO = models.CharField('ФИО', max_length=100)
    Adres = models.TextField('Адрес')

    def __str__(self):
        return self.FIO


    class Meta:
        verbose_name = 'Данные о заказе'
        verbose_name_plural = 'Данные о заказах'
