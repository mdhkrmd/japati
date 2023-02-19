from gpiozero import LED, Button
from signal import pause

led = LED(25)
button = Button(22)

button.when_pressed = led.off
button.when_released = led.on

pause()