from django.conf.urls import patterns, url
from .views import submissions_list, leaderboard, leaderboard_final


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
    url(
        regex=r'^final/$',
        view=leaderboard_final,
        name='leaderboard_final'
    ),
)
