from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from artxivs.models import Artxiv
from artxivs.forms import ArtxivForm

from django.http import HttpResponse

def top(request):
    artxivs = Artxiv.objects.all()
    context = {"artxivs": artxivs}
    return render(request, "artxivs/top.html", context)

@login_required
def artxiv_new(request):
    if request.method == 'POST':
        form = ArtxivForm(request.POST)
        if form.is_valid():
            artxiv = form.save(commit=False)
            artxiv.contributor_name = request.user
            artxiv.save()
            return redirect(artxiv_detail, artxiv_id=artxiv.pk)
    else:
        form = ArtxivForm()
    return render(request, "artxivs/artxiv_new.html", {'form': form})

def artxiv_detail(request, artxiv_id):
    artxiv = get_object_or_404(Artxiv, pk=artxiv_id)
    return render(request, 'artxivs/artxiv_detail.html', {'artxiv':artxiv})

# Create your views here.
