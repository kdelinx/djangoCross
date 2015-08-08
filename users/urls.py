from django.conf.urls import url, patterns


urlpatterns = patterns('users.views',
    url(r'^$', 'profile', name='profile'),
    url(r'edit/$', 'edit_profile', name='edit'),
    url(r'^listing/$', 'user_list', name='listing'),
)
