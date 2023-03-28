#Pomodoro Timer for studying
#Written by InstaLight

# Importing modules
import time
from playsound import playsound

 
# Countdown func
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Times up")
    playsound("alarm.mp3")

print("Welcome to the Pomodoro Study Timer!")
sessions = int(input("Please enter how many study sessions you would like to do today: "))
sessionTime = int(input("Enter the time for each study session in minutes: "))
breakTime = int(input("Enter the time for each break in between sessions in minutes: "))

counter = 1
while(sessions > 0):
    print(f"\nSession: {counter}/{sessions}")
    countdown(sessionTime * 60)
    print("\nBreak")
    countdown(breakTime * 60)
    counter += 1
    sessions -= 1
print("Stuyding finished!")
playsound("finished.mp3")