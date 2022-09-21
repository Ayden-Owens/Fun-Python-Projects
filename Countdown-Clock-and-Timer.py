# Start date 5/26/2022
# It is another utility app in which the user can set a timer, 
# and the app notifies you when time is up.
# End date 5/27/2022

import time
from tkinter import*
from tkinter import messagebox

# Create the interface object
clockWindow = Tk()

# Setting geometry of tk window
clockWindow.geometry("500x500")

# Using title() to display a message in
# the dialogue box of the message in the 
# title bar
clockWindow.title("Countdown Timer")

# Set the background of the window
clockWindow.configure(background='green')

#declare variables
hourStr = StringVar()
minuteStr = StringVar()
secondStr = StringVar()

# Set strings to default value
hourStr.set("00")
minuteStr.set("00")
secondStr.set("00")

# Use the Entry class to take input from user
hourTextbox = Entry(clockWindow, width=3, font=("Arial", 24, ""), textvariable=hourStr)
minuteTextbox = Entry(clockWindow, width=3, font=("Arial", 24, ""), textvariable=minuteStr)
secondTextbox = Entry(clockWindow, width=3, font=("Arial", 24, ""), textvariable=secondStr)

# Center Textboxes
hourTextbox.place(x=170, y=180)
minuteTextbox.place(x=220, y=180)
secondTextbox.place(x=270, y=180)

def runTimer():
    try:
        clockTime = int(hourStr.get())*3600 + int(minuteStr.get())*60 + int(secondStr.get())
    except:
        print("incorrect values")
    
    while(clockTime > -1):
        
        totalMinutes, totalSeconds = divmod(clockTime, 60)
        
        totalHours = 0
        if (totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)
        
        hourStr.set("{0:2d}".format(totalHours))
        minuteStr.set("{0:2d}".format(totalMinutes))
        secondStr.set("{0:2d}".format(totalSeconds))
        
        # Update the interface after decrementing the 
        # clockTime every time
        clockWindow.update()
        time.sleep(1)
        
        # Let the user know if the timer has expired
        if (clockTime == 0):
            messagebox.showinfo("", "Your time is up")
            
        clockTime -= 1

# start the Timer
setTimeButton = Button (clockWindow, text='Set Time Countdown', bd=5, command=runTimer)
setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

# keep looping until 
# an interuption
clockWindow.mainloop()
