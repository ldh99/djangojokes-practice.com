from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Joke

# List view of all jokes 
class JokeListView(ListView):
  model = Joke

# Detail view of a joke inherit from DetailView class
class JokeDetailView(DetailView):
  model = Joke

# Create View to display the joke with data column in html form fields
class JokeCreateView(CreateView):
  model = Joke
  fields = ['question', 'answer']

# Update View to display the joke with data in form fields for update
class JokeUpdateView(UpdateView):
  model = Joke
  fields = ['question', 'answer']
