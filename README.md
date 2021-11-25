# pi-whos-home
led python script, light up led's when an IP becomes live in LAN

6	TASK 12 - WHO IS HOME INDICATOR
LED's were assigned to pins 23, 24 and 25. 

Using PingServer, light up an LED if ping to an ip is successful.  Initial setup was simple enough, however the challenge was to add or modify an ip.  Based on the initial code, I decided to create both a text based menu interface and also a python Tkinter GUI.  Both versions use lists to store values as this is both easy and fast to implement changes while retaining order.  Lists are then combined into a dictionary to be output to console for user when required

## Base code

https://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#who-s-home-indicator

```
from gpiozero import PingServer, LEDBoard
from gpiozero.tools import negated
from signal import pause

status = LEDBoard(
    mum=LEDBoard(red=14, green=15),
    dad=LEDBoard(red=17, green=18),
    alice=LEDBoard(red=21, green=22)
)

statuses = {
    PingServer('192.168.1.5'): status.mum,
    PingServer('192.168.1.6'): status.dad,
    PingServer('192.168.1.7'): status.alice,
}

for server, leds in statuses.items():
    leds.green.source = server
    leds.green.source_delay = 60
    leds.red.source = negated(leds.green)

pause()
```
Link to (not best quality) demonstration video:- https://www.youtube.com/watch?v=nmkSPwR9rUE

### Commits
Have added comments to both versions of the interface to explain the code process more clearly, MIT license has been added since initially did not add a license.   
