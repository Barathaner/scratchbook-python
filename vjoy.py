import pyvjoy
import time

# Assuming vJoy device 1
j = pyvjoy.VJoyDevice(1)
i = pyvjoy.VJoyDevice(2)

while True:
# Set the first button to 'pressed'
    j.set_button(1, 1)

    # Wait for 2 
    j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)



    # Reset the X axis to its center value