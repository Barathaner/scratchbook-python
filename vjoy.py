from pynput import keyboard
import pyvjoy
import time

# Initialize pyvjoy (assuming vJoy driver is installed)
j = pyvjoy.VJoyDevice(1)

current_x = 0x8000  # Start centered
current_y = 0x8000  # Start centered
j.set_axis(pyvjoy.HID_USAGE_X, current_x)
j.set_axis(pyvjoy.HID_USAGE_Y, current_y)
increment = 0x16000  # Increment value
def on_press(key):
    global current_x, current_y
    try:
        if key.char == "w":
            print("up")
            current_y = max(0x0000, current_y - increment)
            j.set_axis(pyvjoy.HID_USAGE_Y, current_y)
            
        if key.char == "a":
            print("left")
            current_x = max(0x0000, current_x - increment)
            j.set_axis(pyvjoy.HID_USAGE_X, current_x)
            
        
        if key.char == "s":
            print("down")
            current_y = min(0x16000, current_y + increment)
            j.set_axis(pyvjoy.HID_USAGE_Y, current_y)
            
        
        if key.char == "d":
            print("right")
            current_x = min(0x16000, current_x + increment)
            j.set_axis(pyvjoy.HID_USAGE_X, current_x)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    current_y = 0x8000
    current_x = 0x8000
    j.set_axis(pyvjoy.HID_USAGE_X, current_x)
    j.set_axis(pyvjoy.HID_USAGE_Y, current_y)

    print('{0} released'.format(
        key))
    

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()