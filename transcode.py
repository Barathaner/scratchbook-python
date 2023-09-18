import subprocess
import cv2
import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import numpy as np

windll.user32.SetProcessDPIAware()
hwnd = win32gui.FindWindow(None, 'Farming Simulator 22')

def capture_frame():
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)

    windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    frame = np.array(im)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return frame

def transcode_video():
    cmd = [
        'ffmpeg',
        '-f', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', '1622x956',  # Größe an Ihre Bildschirmauflösung anpassen
        '-i', '-',
        '-c:v', 'libx264',
        '-crf', '21',
        '-preset', 'veryfast',
        '-g', '50',
        '-keyint_min', '50',
        '-hls_time', '4',
        '-hls_list_size', '0',
        '-hls_flags', 'delete_segments',
        '-force_key_frames', 'expr:gte(t,n_forced*4)',  # Force keyframes every 4 seconds
        '-f', 'hls',
        'C:/Users/User/git/scratchbook-python-2/djangotest/mywebsite/mywebsite/media/stream.m3u8'
    ]




    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    while True:
        frame = capture_frame()
        p.stdin.write(frame.tostring())

transcode_video()
