from django.shortcuts import render

# Create your views here.

from django.views.generic import DetailView, ListView

from .models import Joke

# List view of all jokes 
class JokeListView(ListView):
  model = Joke

# Detail view of a joke inherit from DetailView class
class JokeDetailView(DetailView):
  model = Joke

