from gpiozero import PingServer, LED
from time import sleep
import os

ip = ['192.168.1.1', '192.168.1.239', '192.168.1.187']
user = ['Toni', 'Alex', 'Slava']

hosts = dict(zip(user, ip))

red=LED(23)
green=LED(24)
yellow=LED(25)

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

def close():
    red.source = 0
    green.source = 0
    yellow.source = 0
    quit()
    
def show_all():
    print("These are the current users: \n")
    print(hosts)
    print("Menu will reappear in 5 seconds")
    sleep(5)

def mod_ip():
    global user, ip, hosts
    oldIP = input("Please input the IP to modify: ")
    newIP = input("Please input the new IP: ")
    for index, value in enumerate(ip):
        if value == oldIP:
            ip[index] = newIP
            hosts = dict(zip(user, ip))
            print("IP has been updated: " +str(hosts))
            print("Menu will reappear in 10 seconds")
            sleep(5)    

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
    
def who_is_home():
    try:
        person1 = PingServer(ip[0])
        person2 = PingServer(ip[1])
        person3 = PingServer(ip[2])
        
        red.source = person1.values
        green.source = person2.values
        yellow.source = person3.values
        print("Red led = " +str(user[0]))
        print("Green led = " +str(user[1]))
        print("Yellow led = " +str(user[2]))
        sleep(5)
        
    except KeyboardInterrupt:
        pass
        red.source = 0
        green.source = 0
        yellow.source = 0
        exit()

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
    else:
        # Error message for out of range values entered
        print("Incorrect value used. Try again")
