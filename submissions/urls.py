from django.conf.urls import patterns, url
from .views import submissions_list, leaderboard


urlpatterns = patterns('',

	url(
        regex=r'^show/$',
        view=submissions_list,
        name='list'
    ),
    url(
        regex=r'^leaderboard/$',
        view=leaderboard,
        name='leaderboard'
    ),
)
