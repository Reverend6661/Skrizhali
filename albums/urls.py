from django.conf.urls import url, include
from . import models
from albums import views
import tinymce

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^albums/$', views.album, name='albums'), 
    # url(r'^tinymce/', include('tinymce.urls'), name = 'tinymce-js'),  
    url(r'^albums/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
    url(r'^about/$', views.about, name='about'),    
    url(r'^photos/$', views.photo_album, name='photo_albums'), 
    url(r'^photos/album/(?P<pk>[0-9]+)/$', views.photo_album_detail, name='photo_album_detail'), 
    url(r'^videos/$', views.videos, name='videos'),   
    url(r'^videos/(?P<pk>[0-9]+)/$', views.video_detail, name='video_detail'),
    url(r'^news/$', views.news, name='news'),   
    url(r'^news/(?P<pk>[0-9]+)/$', views.news_detail, name='news_detail'),
  

]


