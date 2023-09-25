import json
from channels.generic.websocket import WebsocketConsumer

# Global state if needed, but it's usually better to avoid global variables if possible.
current_x = 0x8000  # Start centered
current_y = 0x8000  # Start centered

class JoystickConsumer(WebsocketConsumer):
    def connect(self):
        print("WebSocket Connected")
        self.accept()

    def disconnect(self, close_code):
        print("WebSocket Disconnected")

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        
        # Check for the presence of LX and LY (representing the left joystick).
        if 'LX' in data and 'LY' in data:
            self.process_vehicle_control(data['LX'], data['LY'])
        
        # Check for LZ (representing specialized functions of left joystick).
        if 'LZ' in data:
            self.process_special_function(data['LZ'])

        # Check for the presence of RX and RY (representing the right joystick).
        if 'RX' in data and 'RY' in data:
            self.process_camera_control(data['RX'], data['RY'])
            
        # Check for RZ (representing specialized functions of right joystick).
        if 'RZ' in data:
            self.process_special_function(data['RZ'])

        # Check for action commands.
        action = data.get('action')
        if action == 'thumb_control':
            self.process_thumb_control()
        elif action == 'stabilizers':
            self.process_stabilizers()

    def process_thumb_control(self):
        # Handle logic when the thumb control button is pressed.
        print("Thumb Control activated!")

    def process_stabilizers(self):
        # Handle logic when the stabilizers button is pressed.
        print("Stabilizers activated!")

    def process_vehicle_control(self, lx, ly):
        # Process x and y for vehicle control.
        # For example: steering, forward/reverse driving, etc.
        print(f"Vehicle Control - X: {lx}, Y: {ly}")

    def process_camera_control(self, x, y):
        # Process x and y for camera control.
        # For example: changing the player's perspective/view angle.
        print(f"Camera Control - X: {x}, Y: {y}")

    def process_special_function(self, z):
        # Process z for specialized functions.
        # For example: rotating an attachment, pressing shoulder buttons, etc.
        print(f"Special Function - Z: {z}")
