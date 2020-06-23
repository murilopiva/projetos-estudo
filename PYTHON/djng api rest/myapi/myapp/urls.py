
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^musics/$', views.MusicList.as_view(), name='music-list'),
    url('^list/$', views.ListaCompra.as_view(), name='ListaCompra'),
    url('sendmail', sendmail, name='sendmail'),

]