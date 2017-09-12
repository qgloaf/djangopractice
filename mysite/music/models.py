# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    a_artist = models.CharField(max_length=250)
    a_title = models.CharField(max_length=250)
    a_genre = models.CharField(max_length=250)
    a_art = models.CharField(max_length=1000)

class Song(models.Model):
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_filetype = models.CharField(max_length=10)
    song_title = models.CharField(max_length=1000)