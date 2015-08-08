# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractClass(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_update = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Page(AbstractClass):
    page = models.CharField(
        _(u'Название страницы(en)'),
        max_length=64
    )
    title = models.CharField(
        _(u'Заголовок'),
        max_length=255,
    )
    body = models.TextField(
        _(u'Текст страницы')
    )

    class Meta:
        verbose_name = u'Стат. страничка'
        verbose_name_plural = u'Стат. странички'

    def __unicode__(self):
        return self.title
