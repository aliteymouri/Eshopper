from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='دسته بندی')
    image = models.ImageField(upload_to='image/img-categories', null=True, verbose_name='عکس_دسته بندی')
    short_description = models.CharField(max_length=120, verbose_name='توضیح مختصر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان محصول')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image/product', null=True)
    price = models.PositiveIntegerField(verbose_name='قیمت')
    is_active = models.BooleanField(default=True, verbose_name='وضعیت : فعال / غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    slug_address = models.SlugField(unique=True, blank=True, verbose_name='آدرس url محصول')

    def __str__(self):
        return F" عنوان محصول : {self.title}"

    class Meta:
        verbose_name = 'محصول '
        verbose_name_plural = 'محصولات '
