#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Album

# Create your views here.
def index(request):
    html =''
    allAlbums = Album.objects.all()

    for album in allAlbums:
        url = '/music/'+ str(album.id) +'/'
        html += '<a href="' + url +'">'+ album.album_title+'</a>'
    return HttpResponse(html)

def detail(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    return HttpResponse("<h2>Your Requested Album id: " + str(album_id) +"</h2>")