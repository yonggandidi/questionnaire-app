import jwt
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if username is None:
            raise TypeError('Users must have a username.')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email,
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser):

    username = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):

        return self.email

    def get_full_name(self):

        return self.username

    def get_short_name(self):

        return self.username

    @property
    def token(self):

        return self._generate_jwt_token()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
