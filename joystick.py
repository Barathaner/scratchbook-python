import socket
import struct
import time

# Erstellen Sie ein UDP-Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Zieladresse und Port
server_address = ('127.0.0.1', 65010)

while True:
    # Daten gemäß Ihren Vorgaben erstellen
    # Beispielwerte - Sie sollten diese durch Ihre tatsächlichen Werte ersetzen
    joystick1_data = 500, 500, 32767, 32767, 32767, 32767, 32767, 32767
    joystick2_data = 32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767
    joystick1_buttons = 0b10101010101010101010101010101010  # Beispiel für kodierte Tastenwerte

    # Verpacken der Daten in ein Byteformat für die Übertragung
    # Hier verwenden wir uint16 für die Joystickdaten und uint32 für die 
    data_to_send= struct.pack('16HI',500, 500, 32767, 32767, 32767, 32767, 32767, 32767,500, 500, 32767, 32767, 32767, 32767, 32767, 32767,0b10101010101010101010101010101010)
    # Senden Sie die Daten über das Socket
    sock.sendto(data_to_send, server_address)
    #print(data_to_send)
    
    # Warten für 

# Schließen Sie das Socket (dieser Teil wird nie erreicht, da die while-Schleife endlos ist)
