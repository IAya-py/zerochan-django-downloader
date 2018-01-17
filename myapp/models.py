from __future__ import unicode_literals

from django.db import models

class ImageLinks(models.Model):
    imageLocation = models.CharField(max_length = 200)

class ImageDir(models.Model):
    imageDirLoc = models.CharField(max_length = 200)