from django.conf.urls import url
from . import models
from albums import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^albums/$', views.album, name='albums'),   
    url(r'^albums/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
    url(r'^about/$', views.about, name='about'),    
    url(r'^photos/$', views.photo_albums, name='photos'), 
    url(r'^videos/$', views.videos, name='videos'),   
    url(r'^videos/(?P<pk>[0-9]+)/$', views.video_detail, name='video_detail'),
  

]


