import win32gui
import win32ui
from ctypes import windll, wintypes
from PIL import Image
import numpy as np
import cv2

windll.user32.SetProcessDPIAware()
hwnd = win32gui.FindWindow(None, 'Farming Simulator 22')
left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

# Definieren Sie den codec und erstellen Sie ein VideoWriter-Objekt
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (w, h))

try:
    while True:
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
        frame = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

        out.write(frame)
        
        # Ressourcen für diesen Frame freigeben
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)

        # Zeigt den Frame für eine bessere Kontrolle
        cv2.imshow('Recording', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    out.release()
    cv2.destroyAllWindows()
