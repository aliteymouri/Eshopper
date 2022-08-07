from django.contrib import admin
from . import models

admin.site.register(models.Category)


# Register your models here.


@admin.register(models.Product)
class Admin(admin.ModelAdmin):
    list_display = ('__str__', 'is_active')
    list_filter = ('title', 'is_active',)
