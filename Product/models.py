from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    price = models.SmallIntegerField()
    discount = models.SmallIntegerField(null=True,blank=True)
    size = models.ManyToManyField(Size, related_name='products')
    is_active = models.BooleanField()
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save()

    def __str__(self):
        return F" product : {self.title}"
