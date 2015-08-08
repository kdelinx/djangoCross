# coding: utf-8
import uuid
from django.db import models
from django.conf import settings
from core.models import AbstractClass
from users.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill
from django.utils.translation import ugettext_lazy as _


def get_user_avatar(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'avatar/%s%s%s' % (filename[:1], filename[2:3], filename)


class User(AbstractClass, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _(u'E-mail'),
        max_length=150,
    )
    login = models.CharField(
        _(u'Логин'),
        max_length=64,
        unique=True
    )
    first_name = models.CharField(
        _(u'Фамилия'),
        max_length=255
    )
    middle_name = models.CharField(
        _(u'Имя'),
        max_length=255
    )
    third_name = models.CharField(
        _(u'Отчество'),
        max_length=255
    )
    avatar = ProcessedImageField(
        upload_to=get_user_avatar,
        processors=[ResizeToFill(250, 250)],
        format='PNG',
        options={'quality': 85},
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_admin = models.BooleanField(
        default=False
    )
    number = models.IntegerField(
        _(u'Уникальный код'),
        default=0,
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'пользователи'

    def __unicode__(self):
        if not self.first_name or not self.middle_name or not self.third_name:
            return self.login
        else:
            return '%s %s %s' % (self.first_name, self.middle_name, self.third_name)

    def get_full_name(self):
        if not self.first_name or not self.middle_name or not self.third_name:
            return self.login
        else:
            return '%s %s %s' % (self.first_name, self.middle_name, self.third_name)

    def get_short_name(self):
        if not self.first_name or not self.middle_name:
            return self.login
        else:
            return '%s %s.' % (self.first_name, self.middle_name[0])

    def get_avatar_url(self):
        if self.avatar:
            avatar = self.avatar.url
        elif self.is_superuser or self.is_admin:
            avatar = settings.STATIC_URL + 'img/anoavatar.png'
        else:
            avatar = settings.STATIC_URL + 'img/unoavatar.png'
        return avatar

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin