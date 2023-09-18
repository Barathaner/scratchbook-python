# routing.py
from django.urls import re_path
from django.urls import path
from . import consumers
from . import views
from . import ScreenCaptureConsumer
websocket_urlpatterns = [
    path('stream/', views.stream_video, name='stream_video'),
    re_path(r'ws/joystick/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/screen_capture/$', consumers.ScreenCaptureConsumer.as_asgi()),
]