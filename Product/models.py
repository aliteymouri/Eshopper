from django.utils.text import slugify
from django.db import models

from Account.models import User


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='categories', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)

    def __str__(self):
        return F" category : {self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Category, self).save()


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to='products')
    price = models.SmallIntegerField()
    discount = models.SmallIntegerField(null=True, blank=True)
    size = models.ManyToManyField(Size, related_name='sizes', null=True, blank=True)
    is_active = models.BooleanField()
    slug = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save()

    def __str__(self):
        return F" product : {self.title}"


class Comment(models.Model):
    video = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F' comment : {self.text[:30]} / by : {self.author.fullname}'
