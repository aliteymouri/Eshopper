from django.contrib import admin
from . import models


@admin.register(models.Product)
class CateAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")
    list_filter = ("created_at",)
    search_fields = ("title",)
    prepopulated_field = {'slug': ('title',)}


admin.site.register(models.Category)
admin.site.register(models.Size)
admin.site.register(models.Color)
