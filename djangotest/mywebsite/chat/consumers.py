# chat/consumers.py
import json
import pyvjoy
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

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
            
