from django.db import models
from django.urls import reverse

# Create your models here.

class Joke(models.Model):
  question = models.TextField(max_length=200)
  answer = models.TextField(max_length=100, blank=True)
  # auto_now_add=True - field will automatically be assigned 
  # current date and time when the row is created
  created = models.DateTimeField(auto_now_add=True)
  # auto_now=True - value of field will be changed to current
  # date and time when the row is updated
  updated = models.DateTimeField(auto_now=True)

  # alertnative to constructing URLs with get_absolute_url() method
  # define below to called in the templates\jokes\joke_list.html as 
  # href="{{ joke.get_absolute_url }}"> instead of
  # href="{% url 'jokes:detail' joke.pk %}">

  def get_absolute_url(self):
    return reverse('jokes:detail', args=[str(self.pk)])
  
  # __str__() method - return output of the row convert to a string
  def __str__(self):
    return self.question
