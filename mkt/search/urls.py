from django.conf.urls.defaults import patterns, url

from search.views import ajax_search_suggestions, WebappSuggestionsAjax
from . import views


urlpatterns = patterns('',
    url('^$', views.app_search, name='search.search'),
    url('^ajax/apps$', views.ajax_search, name='search.apps_ajax'),
    url('^suggestions$', ajax_search_suggestions,
        name='search.suggestions'),
)
