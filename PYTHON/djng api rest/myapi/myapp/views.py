from django.shortcuts import render
from rest_framework import generics
from .models import Music, Lista
from .serializers import MusicSerializer, JsonListaCompras

# Create your views here.
class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class ListaCompra(generics.ListCreateAPIView):

    queryset = Lista.objects.all()
    serializer_class = JsonListaCompras

