# urls path for pages app

from django.urls import path
from django.urls.resolvers import URLPattern

from .views import AboutUsView, HomePageView

app_name = 'pages'
urlpatterns = [
  path('', HomePageView.as_view(), name='homepage'),
  path('about-us/', AboutUsView.as_view(), name='about-us'),
]