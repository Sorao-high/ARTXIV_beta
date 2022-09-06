from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from artxivs.models import Artxiv
from artxivs.forms import ArtxivForm

from django.http import HttpResponse

class top(ListView):
     template_name = 'artxivs/top.html'
     context_object_name = 'artxivs'
     model = Artxiv

     def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            artxivs = Artxiv.objects.filter(
                Q(title__icontains=q_word) | Q(artist_name__icontains=q_word)| Q(abstract__icontains=q_word))
        else:
            artxivs = Artxiv.objects.all()
            
        return artxivs

@login_required
def artxiv_new(request):
    if request.method == 'POST':
        form = ArtxivForm(request.POST, request.FILES)
        if form.is_valid():
            artxiv = form.save()
            artxiv.contributor_name = str(request.user)
            artxiv.save()
            return redirect(artxiv_detail, artxiv_id=artxiv.pk)
    else:
        form = ArtxivForm()
    return render(request, "artxivs/artxiv_new.html", {'form': form})

def artxiv_detail(request, artxiv_id=0):
    artxiv = get_object_or_404(Artxiv, pk=artxiv_id)
    return render(request, 'artxivs/artxiv_detail.html', {'artxiv':artxiv})

# Create your views here.
