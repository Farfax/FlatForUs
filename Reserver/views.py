from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Flat, Town
from django.views import generic

class IndexView(generic.ListView):
    template_name = "Reserver/index.html"
    context_object_name = 'town_list'

    def get_queryset(self):
        return Town.objects.all()

class DetailView(generic.DetailView):
    #model=Flat
    template_name = 'Reserver/detail.html'
    context_object_name = 'flat_list' 
    def get_queryset(self):
        return Flat.objects.all()

class ResultsView(generic.DetailView):
    #model= Flat
    template_name= 'Reserver/results.html'

# Create your views here.
