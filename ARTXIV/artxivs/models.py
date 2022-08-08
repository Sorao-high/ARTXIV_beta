from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from django import forms

class Artxiv(models.Model):
    artist_statement = models.ImageField(upload_to='uploads/%Y/%m/%d/',)
    title = models.CharField('Title', max_length=100)    
    artist_name = models.CharField('Artist name', max_length=20) 
    contributor_name = models.CharField('Contributor name', max_length=20)
    abstract = models.CharField('Abstract', max_length=1000)
    exhibition_histry = models.CharField('Exhibition histry', max_length=200)
    posted_at = models.DateTimeField("Post day", auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
