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
import xml.etree.ElementTree as ET

global current_x,current_y
j = pyvjoy.VJoyDevice(1)
a = 0

for i in range(0, 9):
    j = pyvjoy.VJoyDevice(i)
    if j.get_axis(pyvjoy.HID_USAGE_X) != 0:
        a = i
        break
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
    
    
class XmlParserConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connected = True

    def sendXmlData(self):
        xml_path = "C:/Users/User/Documents/My Games/FarmingSimulator2022/mods/FS22_karl/VehicleInfoPrinter.xml"  # Pfad zu deiner XML-Datei
        while self.connected:
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                json_data = self.xml_to_json(root)
                self.send(text_data=json.dumps(json_data))
                time.sleep(0.5)  # Warte 2 Sekunden vor dem nächsten Senden

            except ET.ParseError:
                # Optional: Fehlermeldung an den Client senden
                self.send(text_data=json.dumps({"error": "Fehler beim Parsen der XML-Datei."}))

    def xml_to_json(self, root):
        data = {}
        if root.tag == 'VehicleInfoPrinter':
            for elem in root:
                if elem.tag == 'controlledVehicle':
                    data['controlledVehicle'] = {child.tag: child.text for child in elem}
                elif elem.tag == 'playerPosition':
                    data['playerPosition'] = {k: v for k, v in elem.attrib.items()}
        return data

    def connect(self):
        self.accept()
        # Startet den XML-Parser in einem separaten Thread
        threading.Thread(target=self.sendXmlData).start()

    def disconnect(self, close_code):
        self.connected = False

    def receive(self, text_data):
        # Hier können zusätzliche Funktionen hinzugefügt werden, je nachdem, wie der Client mit dem Server interagieren soll.
        pass