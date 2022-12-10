from django.db import models

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

  # __str__() method - return output of the row convert to a string
  def __str__(self):
    return self.question
