# coding: utf-8
import simplejson
from game.models import Game, Score
from users.models import User
from django.shortcuts import (render, get_object_or_404,
                              HttpResponseRedirect, Http404,)
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required
def list_score(request):
    score = Score.objects.order_by('-score', 'id')
    context = {
        'score': score,
    }
    return render(request, 'game/list_score.html', context)


@login_required
def game_init(request):
    return render(request, 'game/game.html')


@login_required
def create_game(request, id):
    user = request.user.id
    game = get_object_or_404(Game)
    if request.POST:
        init = Game(first_user=user, second_user=game.second_player.id)
        init.save()
        return HttpResponseRedirect(
            reverse('game:game', args=(game.second_player.id,))
        )



@login_required
def connect_game(request, id):
    pass