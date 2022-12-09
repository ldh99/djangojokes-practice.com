from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

# Home page template
class HomePageView(TemplateView):
  template_name = 'pages/home.html'

# About_Us template
class AboutUsView(TemplateView):
  template_name = 'pages/about_us.html'