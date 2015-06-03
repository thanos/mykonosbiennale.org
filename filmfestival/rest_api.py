# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


from rest_framework import routers, serializers, viewsets
from rest_framework import generics

import models

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Film
        depth = 2
    filmfestival_image_related = ImageSerializer(many=True, read_only=True)
    
class FilmView(generics.ListAPIView):
    queryset = models.Film.objects.exclude(filmfestival_image_related= None).order_by('ref')
    serializer_class = FilmSerializer
    
    
    