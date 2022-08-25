from dataclasses import field
#from socket import fromshare iosだと必要ないかも
from django import forms

from artxivs.models import Artxiv

class ArtxivForm(forms.ModelForm):
    class Meta:
        model = Artxiv
        fields = ('title', 'artist_name', 'artist_statement', 'abstract', 'exhibition_histry')
