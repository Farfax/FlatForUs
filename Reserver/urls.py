from django.conf.urls import url

from . import views

app_name = 'Reserver'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[a-zA-Z]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^Warszawa/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    ]
