from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from .models import User, Otp


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'fullname', 'phone', 'is_admin', 'is_active',)
    list_filter = ('is_active', 'is_admin')

    fieldsets = (
        ('مشخصات', {'fields': ('email', 'fullname', 'phone', 'image', 'password',)}),
        ('دسترسی ها', {'fields': (
            'is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}
         ),
    )

    add_fieldsets = (
        (None, {'fields': (
            'email', 'fullname', 'phone', 'password', 'confirm_password')}
         ),
    )

    search_fields = ('phone', 'email', 'fullname')
    ordering = ('-date_joined',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disable = True
        return form


admin.site.register(User, UserAdmin)
admin.site.register(Otp)
