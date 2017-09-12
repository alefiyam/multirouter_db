# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import six, timezone
from django.contrib.auth.validators \
    import ASCIIUsernameValidator, UnicodeUsernameValidator
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from django.conf import settings

DATABASE_CHOICES = []
for key, value in settings.DATABASES.items():
    val = key
    if key == 'default':
        val = 'default_database'
    DATABASE_CHOICES.append((key, val))


class Database(models.Model):
    name = models.CharField(
        max_length=100, choices=DATABASE_CHOICES, default='database1')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    _DATABASE = "default"


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator(
    ) if six.PY3 else ASCIIUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'))
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    databases = models.ManyToManyField(Database)

    def list_databases(self):
        return ', '.join([name.name for name in self.databases.all()])

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail("credentials", "hello",
                  "alefiya.malik07@gmail.com", [self.email], **kwargs)

    _DATABASE = "default"


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    _DATABASE = "default"


class Product(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)
    price = models.FloatField(null=False, blank=False)
    user_id = models.IntegerField(null=False, blank=False, default=None)


from django.core.mail.message import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import password_reset


@receiver(post_save, sender=User)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    try:
        first_name = instance.username
        password = instance.password
        email = instance.email
        html_content = "your username:%s <br> password reset link:%s"
        message = EmailMessage(subject='welcome', body=html_content %
                               (first_name, password), to=[email])
        message.send()
    except Exception as e:
        print e
