from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^albums/$', views.album, name='albums'),
    url(r'^albums/$', views.album, name='albums'),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
]

