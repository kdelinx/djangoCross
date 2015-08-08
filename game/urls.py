from django.conf.urls import patterns, url

urlpatterns = patterns('game.views',
    url(r'^score/$', 'list_score', name='score'),
    url(r'^game/$', 'game_init', name='game'),
    url(r'^create_with_(?P<id>\d+)/$', 'create_game', name='create'),
)