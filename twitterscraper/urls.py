from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^results/$', views.results, name='results'),
    url(r'^tableresults/$', views.tableresults, name='tableresults'),
    url(r'^details/$', views.details, name='details'),
    url(r'^count/$', views.count, name='count'),
]
