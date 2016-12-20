from django.http import HttpResponse
from .models import Album
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'index.html')

def album(request):
    return render(request, 'albums/album_list.html', {'album': album})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})