from django.urls import path

from .views import (
  JokeListView, JokeDetailView, JokeCreateView, JokeUpdateView
)

app_name = 'jokes'
urlpatterns = [
  # url as jokes/
  path('', JokeListView.as_view(), name='list'),
  
  # path joke/<int:pk>/ indicates that the value entered for this
  # part of the path must be an integer. 
  # The view has access to this value via self.kwargs.get('pk') 
  # and will use it to get the specific joke object to use
  # url as jokes/joke/2
  path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),

  # path to update joke urls as example jokes/joke/2/update
  path('joke/<int:pk>/update', JokeUpdateView.as_view(), name='update'),

  # path to create joke with rul as jokes/joke/create
  path('joke/create', JokeCreateView.as_view(), name='create'),
]
