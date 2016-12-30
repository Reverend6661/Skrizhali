# -*- coding: utf-8 -*- 
from django.http import HttpResponse
from albums.models import Album
from videos.models import Videos
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage

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
    return render(request, 'index.html')

# Дискография
def album(request):
	album_list = Album.objects.all().order_by('release_year')
	for album in album_list:
		album.cover = str(album.cover).split('/')[-1]

	return render(request, 'albums/album_list.html', {'album_list': album_list})

def album_detail(request, pk):    
    album = get_object_or_404(Album, pk=pk)
    album.cover = str(album.cover).split('/')[-1]
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














# Mailchimp send mail
def envEmail(request):
	mes = EmailMessage(subject="Subject", from_email="sergeypugach18@gmail.com", to=['sergeypugach18@gmail.com'])
	mes.template_name='template1'
	mes.template_content = {
		'user': u"AdministratorSlide17"
	}
	mes.send()
	return render(request, 'confirmation.html')
