import json
from channels.generic.websocket import WebsocketConsumer
import base64
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


class ScreenCaptureConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:  # Dies startet einen unendlichen Loop, um kontinuierlich den Bildschirm zu erfassen
            frame = capture_frame()
            _, buffer = cv2.imencode('.jpg', frame)
            encoded_image = base64.b64encode(buffer).decode('utf-8')

            self.send(text_data=json.dumps({
                'image': encoded_image
            }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # Dies wird getriggert, wenn Daten vom Frontend empfangen werden
        # Hier können Sie die Bildschirmaufnahme-Funktion implementieren
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
