# pi-whos-home
(Completed) Led python script, light up led's when an IP becomes live in LAN

WHO IS HOME INDICATOR
LED's were assigned to pins 23, 24 and 25. 

Using PingServer, light up an LED if ping to an ip is successful.  Check the example code (Base code) and configure a GUI to modify the IP.  

## Thought Process
Rather than just jump in to the above task I decided to implement this as a text-based interface, this way I could identify functions and then base my GUI from this.
As can be seen from below, the base code was not very pliable when it comes to making alterations, so I redesigned the code to modify users and IP values.  Text based interface code is shown below base code, you can compare versions to see how much difference there is to original recipe.  Users and IP values are now stored in 2 separate lists, those 2 lists are then combined to a single dictionary, this meant altering either IP or User was much easier to perform and retains correct order, once modifications were completed, lists were then recompiled to a dictionary which could be printed to console to check the current stored values, with the text based version completed and working, I then used the functions to build a working GUI.  This went a little beyond the scope of the original scenario but I like to think my version is much easier to change and offers a lot more functionality, while at the same time increasing my knowledge of both python & Tkinter.

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

## Text menu interface code
```
#Text based menu interface for who is home LED indicator.
from gpiozero import PingServer, LED
from time import sleep
import os

#generic values updated, this way you can then configure at initial run.
ip = ['10.0.0.0', '10.1.1.1', '10.2.2.2']
user = ['user1', 'user2', 'user3']

#creates a dictionary from the 2 lists above
hosts = dict(zip(user, ip))

#assign pins for the LEDs
red=LED(23)
green=LED(24)
yellow=LED(25)

#create text based menu
def print_menu():
    print("***************************************************")
    print("Who's home module, add/remove/modify hosts and IPs")
    print("***************************************************")
    print("Choose one of the  options below: \n")

    print("1: List current users and their IP.")
    print("2: Modify the IP of an existing user.")
    print("3: Change a user name.")
    print("4: Check who is currently home.")
    print("5: Close the app.")

#turn off all LEDs when app is closed
def close():
    red.source = 0
    green.source = 0
    yellow.source = 0
    quit()

#print current listing of dictionary
def show_all():
    print("These are the current users: \n")
    print(hosts)
    print("Menu will reappear in 5 seconds")
    sleep(5)

#function to modify an IP, find the old value and modify with new value
#e.g. oldIP = 10.0.0.0 and replace with value for newIP 192.168.1.30
def mod_ip():
    global user, ip, hosts
    oldIP = input("Please input the IP to modify: ")
    newIP = input("Please input the new IP: ")
#check list for old value, replace with new value and rebuild dictionary
    for index, value in enumerate(ip):
        if value == oldIP:
            ip[index] = newIP
            hosts = dict(zip(user, ip))
            print("IP has been updated: " +str(hosts))
            print("Menu will reappear in 10 seconds")
            sleep(5)    

#replace username using similar method to above
def mod_host():
    global user, ip, hosts
    name = input("Name of user to rename: ")
    newName = input("New name to use: ")
    for index, value in enumerate(user):
        if value == name:
            user[index] = newName
        else:
            print("User is not listed, please try again.")
            break
    hosts = dict(zip(user, ip))
    print("User has been updated: " +str(hosts))
    print("Menu will reappear in 5 seconds")
    sleep(5)

#run pingserver to ping the IP values in the list, if IP is live, light the corresponding LED
def who_is_home():
    try:
        person1 = PingServer(ip[0])
        person2 = PingServer(ip[1])
        person3 = PingServer(ip[2])
        
        red.source = person1.values
        green.source = person2.values
        yellow.source = person3.values
#inform via console which user has been assigned to which LED
        print("Red led = " +str(user[0]))
        print("Green led = " +str(user[1]))
        print("Yellow led = " +str(user[2]))
        sleep(5)
        
#except statement added and reset LEDs
    except KeyboardInterrupt:
        pass
        red.source = 0
        green.source = 0
        yellow.source = 0
        exit()

#loop so that app constantly runs until closed
loop = True
while loop:
    print_menu()
    choice = input("Please choose one of the numbered options: ")
    if choice=='1':     
        print("List all users and IP's")
        show_all()
    elif choice=='2':
        print("Modify an IP")
        mod_ip()
    elif choice=='3':
        print("Change a host name")
        mod_host()
    elif choice=='4':
        print("Check who is home?")
        who_is_home()
    elif choice=='5':
        print("Exit the program")
        close()
        loop=False
#else statement added for anything pressed other than 1 through 5
    else:
        # Error message for out of range values entered
        print("Incorrect value used. Try again")
```

## Demo of Tkinter GUI code 

Link to (not best quality) demonstration video of Tkinter GUI:- https://www.youtube.com/watch?v=nmkSPwR9rUE


### Commits
Have added comments to both versions of the interface to explain the code process more clearly, MIT license has been added since initially did not add a license, Readme has been updated to include link to demo of the Tkinter GUI from youtube, and renaming the files to more clearly reflect their task.   
