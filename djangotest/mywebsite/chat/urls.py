from django.urls import path
from . import views
 
urlpatterns = [
    path('stream/', views.stream_video, name='stream_video'),
 ]
 