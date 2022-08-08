from django.urls import path

from artxivs import views

urlpatterns = [
    path("new/", views.artxiv_new, name="artxiv_new"),
    path("<int:artxiv_id>/", views.artxiv_detail, name="artxiv_detail"),
]