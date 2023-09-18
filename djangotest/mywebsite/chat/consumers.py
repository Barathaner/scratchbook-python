# chat/consumers.py
import json
import pyvjoy
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import time
import json
from channels.generic.websocket import WebsocketConsumer
import base64
import cv2
import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import numpy as np
import threading

global current_x,current_y
j = pyvjoy.VJoyDevice(1)
current_x = 0x8000  # Start centered
current_y = 0x8000  # Start centered
incrementvalue = 0x16000  # Increment value
class ChatConsumer(WebsocketConsumer): 
    def connect(self):
        print("connected")
        j = pyvjoy.VJoyDevice(1)


        j.set_axis(pyvjoy.HID_USAGE_X, current_x)
        j.set_axis(pyvjoy.HID_USAGE_Y, current_y)
        
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        print("disconnected")

    # Receive message from WebSocket
    def receive(self, text_data):
        global current_x, current_y
        j = pyvjoy.VJoyDevice(1)
        text_data_json = json.loads(text_data)
        direction = text_data_json['direction']
        isPressed = text_data_json["isPressed"]
        
        if isPressed:
            if direction == "up":
                print("up")
                current_y = max(0x0000, current_y - incrementvalue)
                j.set_axis(pyvjoy.HID_USAGE_Y, current_y)
                
            if direction == "left":
                print("left")
                print(current_x)
                current_x = max(0x0000, current_x - incrementvalue)
                j.set_axis(pyvjoy.HID_USAGE_X, current_x)
                
            
            if direction == "down":
                print("down")
                current_y = min(0x16000, current_y + incrementvalue)
                j.set_axis(pyvjoy.HID_USAGE_Y, current_y)
                
            
            if direction == "right":
                print("right")
                current_x = min(0x16000, current_x + incrementvalue)
                j.set_axis(pyvjoy.HID_USAGE_X, current_x)
        else:
            print("released")
            current_y = 0x8000
            current_x = 0x8000
            j.set_axis(pyvjoy.HID_USAGE_X, current_x)
            j.set_axis(pyvjoy.HID_USAGE_Y, current_y)
            


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
    frame = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return frame



    
class ScreenCaptureConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connected = True
    
    def sendVideo(self):
        while self.connected:
            frame = capture_frame()
            _, buffer = cv2.imencode('.jpg', frame)
            encoded_image = base64.b64encode(buffer).decode('utf-8')

            self.send(text_data=json.dumps({
                'image': encoded_image
            }))
            time.sleep(0.03)  # Einen kurzen Sleep hinzufügen, um nicht ständig zu senden.
    
    def connect(self):
        self.accept()
        # Startet den Video-Sendemechanismus in einem separaten Thread
        threading.Thread(target=self.sendVideo).start()

    def disconnect(self, close_code):
        self.connected = False

    def receive(self, text_data):
        # ... Rest des Codes bleibt unverändert
        pass