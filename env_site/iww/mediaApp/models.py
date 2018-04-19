from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=50)
    content = models.CharField(max_length=256)
    publicationDate = models.DateField()
    #tells Python how to display a human-readable representation of an object
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['publicationDate']
