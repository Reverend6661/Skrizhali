# -*- coding: utf-8 -*-
from django.http import HttpResponse
from albums.models import Album
from videos.models import Videos
from photo_albums.models import Photo_album, Photo
from news.models import News
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.utils.html import format_html


"""
Новости
О группе
Дискография
Фото
Видео
Контакты
Ссылки
"""

# Заглавная страница с новостями
def index(request):
	news_list = News.objects.all().order_by('created_date')
	return render(request, 'index.html', {'news_list': news_list})

# Дискография
def album(request):
	album_list = Album.objects.all().order_by('release_year')
	for album in album_list:
		album.cover = str(album.cover).split('/')[-1]

	return render(request, 'albums/album_list.html', {'album_list': album_list})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.cover = str(album.cover).split('/')[-1]
    album.songs_list = format_html(album.songs_list)
    return render(request, 'albums/album_detail.html', {'album': album})

# О группе
def about(request):
	return render(request, 'about.html')

def photo_albums(request):
	return render(request, 'photo_albums/index.html')


def videos(request):
	video_list = Videos.objects.all().order_by('date')
	for video in video_list:
		video.link = str(video.link).split('=')[-1]
	return render(request, 'videos/video_list.html', {'video_list': video_list})

def video_detail(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    video.link = str(video.link).split('=')[-1]
    return render(request, 'videos/video_detail.html', {'video': video})

def news(request):
	news_list = News.objects.all().order_by('-created_date')
	news_list = news_list[0:5]
	return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.image = str(news.image).split('/')[-1]
    return render(request, 'news/news_detail.html', {'news': news})

def photo_album(request):
	photo_album_list = Photo_album.objects.all()
	cover_photo = Photo.objects.all()[0]
	return render(request, 'photo_albums/photo_album_list.html', {'photo_album_list': photo_album_list, 'cover_photo': cover_photo})

def photo_album_detail(request, pk):
    photo_album = get_object_or_404(Photo_album, pk=pk)
    photos_list = Photo.objects.filter(photo_album=photo_album)
    return render(request, 'photo_albums/photo_album_detail.html', {'photo_album': photo_album, 'photos_list': photos_list})
