# coding: utf-8
from django.db import models
from core.models import AbstractClass
from users.models import User
from django.utils.translation import ugettext_lazy as _


class Score(AbstractClass):
    user = models.ForeignKey(
        User,
        verbose_name=_(u'Пользователь'),
        related_name='user_score'
    )
    score = models.SmallIntegerField(
        _(u'Количество балов')
    )

    class Meta:
        verbose_name = u'Таблица результата'
        verbose_name_plural = u'Таблица результатов'

    def __unicode__(self):
        return '%s - %s' % (self.user.get_short_name(), self.score)


class Game(AbstractClass):
    first_player = models.ForeignKey(
        User,
        verbose_name=_(u'First user'),
        related_name='first_user_game'
    )
    second_player = models.ForeignKey(
        User,
        verbose_name=_(u'Second user'),
        related_name='second_user_game'
    )
    x1 = models.SmallIntegerField(
        verbose_name=_(u'row 1 cell 1')
    )
    x2 = models.SmallIntegerField(
        verbose_name=_(u'row 1 cell 2')
    )
    x3 = models.SmallIntegerField(
        verbose_name=_(u'row 1 cell 3')
    )
    x4 = models.SmallIntegerField(
        verbose_name=_(u'row 2 cell 1')
    )
    x5 = models.SmallIntegerField(
        verbose_name=_(u'row 2 cell 2')
    )
    x6 = models.SmallIntegerField(
        verbose_name=_(u'row 2 cell 3')
    )
    x7 = models.SmallIntegerField(
        verbose_name=_(u'row 3 cell 1')
    )
    x8 = models.SmallIntegerField(
        verbose_name=_(u'row 3 cell 2')
    )
    x9 = models.SmallIntegerField(
        verbose_name=_(u'row 3 cell 3')
    )

    class Meta:
        verbose_name = u'Игровой процесс'
        verbose_name_plural = u'Игровой процесс'

    def __unicode__(self):
        if not self.second_player:
            return '%s vs. ???' % (self.first_player.get_short_name())
        else:
            return '%s vs. %s' % (self.first_player.get_short_name(),
                                  self.second_player.get_short_name())