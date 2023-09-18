from django.http import FileResponse
from django.conf import settings
import os

def stream_video(request):
    file_path = 'C:/Users/User/git/scratchbook-python-2/djangotest/mywebsite/mywebsite/media/stream.m3u8'
    return FileResponse(open(file_path, 'rb'), content_type="application/vnd.apple.mpegurl")
