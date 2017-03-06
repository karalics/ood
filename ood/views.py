from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpRequest as request
from django.views import generic
from django.views.generic.edit import CreateView
from django import forms
from django.shortcuts import render
from django.views.generic.edit import ModelFormMixin


from .forms import SatzForm
from .models import OODBeispiel


class CreateView(generic.CreateView):
    def get_initial(self):
        initial = super(CreateView, self).get_initial()
        initial = {
        'beispielsatz': self.request.GET.get('bspsatz'),
	}
        satz = self.request.GET.get('bspsatz')
        s = OODBeispiel(beispielsatz=satz)
        s.save()
        return initial 

        
    model = OODBeispiel
    fields = ['beispielsatz']
    success_url = '/add-satz/'

class IndexView(generic.ListView):
    model = OODBeispiel
    template_name = 'index.html'
    context_object_name = 'latest_ood_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return OODBeispiel.objects.all

class DetailView(generic.DetailView):
    model = OODBeispiel
    template_name = 'satz.html'




