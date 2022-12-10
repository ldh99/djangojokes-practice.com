from django.urls import path

from .views import JokeListView, JokeDetailView

app_name = 'jokes'
urlpatterns = [
  path('', JokeListView.as_view(), name='list'),
  
  # path joke/<int:pk>/ indicates that the value entered for this
  # part of the path must be an integer. 
  # The view has access to this value via self.kwargs.get('pk') 
  # and will use it to get the specific joke object to use
  path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
]
