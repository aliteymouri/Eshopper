from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, fullname, phone, password):
        if not phone:
            raise ValueError('وارد کردن شماره تلفن  الزامی میباشد')

        elif not email:
            raise ValueError('وارد کردن ایمیل الزامی میباشد')

        user = self.model(

            email=self.normalize_email(email),
            fullname=fullname,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, phone, password):
        user = self.create_user(email, fullname, phone, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
