import json
from channels.generic.websocket import WebsocketConsumer



class ScreenCaptureConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

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
