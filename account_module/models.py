from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    avatar = models.ImageField(upload_to='image/users_profile',null=True, verbose_name='عکس کاربری')
    biography = models.CharField(max_length=130, verbose_name='بیوگرافی')

    def __str__(self):
        return F" نام : {self.user.get_full_name()}"

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'
