from rest_framework import serializers
from .models import Music, Lista

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = '__all__'

class JsonListaCompras(serializers.ModelSerializer):

    class Meta:

        model = Lista
        fields = '__all__'

