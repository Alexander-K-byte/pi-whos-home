from gpiozero import PingServer, LED
from time import sleep
from tkinter import *
import tkinter.messagebox

#create the initial Window for our GUI
window = Tk()
window.title("Who's home LED indicator")
window.geometry("400x320")

#Define global list
#List used since easier to change value than changing key from a dictionary and keeping value/order
ip = ['192.20.49.11', '192.20.50.143', '192.20.49.13']
user = ['Toni', 'Alex', 'Slava']
#Define global dictionary from the lists
hosts = dict(zip(user, ip))

red=LED(23)
green=LED(24)
yellow=LED(25)

def close():
    #Turn off all LED's and close the application
    red.source = 0
    green.source = 0
    yellow.source = 0
    quit()
    
def show_all():
    #print output of the 2 lists stored in global dictionary
    print("These are the current users: \n")
    print(hosts)
    
def mod_ip_input():
    #reference the global lists/dictionary
    global user, ip, hosts
    #variable used in method of halting program code to wait on submit being pressed
    var=IntVar()
    #create new TopLevel window for text input
    ipWindow = Toplevel(window)
    ipWindow.title("Change an IP")
    ipWindow.geometry("350x250")
    #create label to show user what text entry box is for
    IP1 = Label(ipWindow, text="Enter old IP value:")
    #pady used to space out the items vertically
    IP1.pack(side = TOP,pady=15)
    #create text entry box with border feature for more appealing look
    old = Entry(ipWindow, bd =5)
    old.pack(side = TOP)
    IP2 = Label(ipWindow, text="Enter new IP value:")
    IP2.pack(pady=15)
    new = Entry(ipWindow, bd =5)
    new.pack()
    #submit button has lambda var to pause program so that it will read
    #the values typed in after submit button is pressed
    #Prevents .get() reading blank lines
    button = Button(ipWindow, text="Submit", command=lambda: var.set(1))
    button.pack(pady=15)
    #pause program to wait for button press
    button.wait_variable(var)
    #read text typed into entry boxes and stringify (Not sure if str() required
    oldIP = str(old.get())
    newIP = str(new.get())
    #go through list searching for the index number and value of the search term
    for index, value in enumerate(ip):
        if value == oldIP:
            #if the value is found, change the value at the index to be the new term
            ip[index] = newIP
            hosts = dict(zip(user, ip))
            print("Current host/IP: " +str(hosts))
            #display popup box so user knows it has worked
            tkinter.messagebox.showinfo(title='It worked', message='IP has been modified')
        #Destroys toplevel window even if value not found and changed
        ipWindow.destroy()
    
def mod_host_input():
    #exactly the same process as modifying IP but for the user list instead
    global user, ip, hosts
    var=IntVar()
    hostWindow = Toplevel(window)
    hostWindow.title("Change a user")
    hostWindow.geometry("350x250")
    user1 = Label(hostWindow, text="Type name to change:")
    user1.pack(side = TOP,pady=15)
    oldUser = Entry(hostWindow, bd =5)
    oldUser.pack(side = TOP)
    user2 = Label(hostWindow, text="Enter new name:")
    user2.pack(pady=15)
    newUser = Entry(hostWindow, bd =5)
    newUser.pack()
    button = Button(hostWindow, text="Submit", command=lambda: var.set(1))
    button.pack(pady=15)
    button.wait_variable(var)
    name = str(oldUser.get())
    newName = str(newUser.get())
    for index, value in enumerate(user):
        if value == name:
            user[index] = newName
            hosts = dict(zip(user, ip))
            print("Current host/IP: " +str(hosts))
            tkinter.messagebox.showinfo(title='It worked', message='Name has been modified')
        hostWindow.destroy()
        
def who_is_home():
    try:
        #If ip is updated, will need to be ran again
        #generic person used and Pingserver uses ip list index to find values needed to ping
        person1 = PingServer(ip[0])
        person2 = PingServer(ip[1])
        person3 = PingServer(ip[2])
        #on run will update led's if IP's are correct, did not require pause function
        #if pause is used, it will just hang the app on this once pressed
        red.source = person1.values
        green.source = person2.values
        yellow.source = person3.values
        print("Red led = " + str(user[0]))
        print("Green led = " + str(user[1]))
        print("Yellow led = " + str(user[2]) +"\n")
        sleep(5)
        
    except KeyboardInterrupt:
        #Set all LEDs to off on keyboard interrupt
        pass
        red.source = 0
        green.source = 0
        yellow.source = 0
        exit()

#map all the functions to buttons for master frame
show_button = Button(window, text="show all users/IPs", command=show_all)
show_button.pack(pady=15)
userMod_button = Button(window, text="change a username", command=mod_host_input)
userMod_button.pack(pady=15)
ipMod_button = Button(window, text="modify IP address", command=mod_ip_input)
ipMod_button.pack(pady=15)
whoDat_button = Button(window, text="Check who is home", command=who_is_home)
whoDat_button.pack(pady=15)
quit_button = Button(window, text="Close the program", command=close)
quit_button.pack(pady=15)
mainloop()
