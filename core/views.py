# coding: utf-8
from itertools import chain
from core.models import Page
from game.models import Score, Game
from users.models import User
from django.shortcuts import (render,
                              get_object_or_404,
                              HttpResponseRedirect,)
from django.core.urlresolvers import reverse


def error404(request):
    return render(request, 'core/404.html')


def page(request, page):
    article = get_object_or_404(Page, page=page)
    context = {
        'page': Page.objects.get(page=article.page),
    }
    return render(request, 'core/static.html', context)


def index(request):
    score_list = Score.objects.order_by('-score')
    # result_list = sorted(chain(score_list),
    #                      key=lambda x: x.score, reverse=True)
    context = {
        # 'result_list': result_list,
        'result_list': score_list,
    }
    return render(request, 'core/index.html', context)