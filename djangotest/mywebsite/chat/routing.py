# routing.py
from django.urls import re_path
from django.urls import path

#from . import ScreenCaptureConsumer
from . import consumers
from . import views

websocket_urlpatterns = [
    path('stream/', views.stream_video, name='stream_video'),
    re_path(r'ws/joystick/$', consumers.JoystickConsumer.as_asgi()),
    path('ws/xmlparser/', consumers.JoystickConsumer.as_asgi()),
    #re_path(r'ws/screen_capture/$', ScreenCaptureConsumer.ScreenCaptureConsumer.as_asgi()), 
    
]