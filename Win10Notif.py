from win10toast import ToastNotifier
import random
import threading

notifInterval = int(input("How often would you like to receive notifications? (in seconds): ")) # Asks the user how often they'd like to receive notifications and stores the input as an integer.
notifDuration = int(input("How long would you like each notification to be displayed for? (in seconds): ")) # Asks the user how long they'd like each notification to be displayed for and stores the input as an integer.

# ---------- USER CONFIGURABLE SECTION -----------------
notifTitles = ["Boop", "Beep"] # Array used for storing the notification titles. Make sure to change the values for your use case.
notifDescriptions = ["Blurp", "Blarp"]  # Array used for storing the notification descriptions. Make sure to change the values for your use case.
# ---------- END OF USER CONFIGURABLE SECTION ----------

def notif():
    notifTitle = random.choice(notifTitles) # Randomly chooses a notification title from the notifTitle array.
    notifDescription = random.choice(notifDescriptions) # Randomly chooses a notification title from the notifDescription array.
    timer = threading.Timer(notifInterval, notif) # Sets timer variable as threading.Timer() function imported from threading, using the integer collected from notifInterval as the timer length and the notif function as the thing that's being timed.
    toast = ToastNotifier() # Sets toast variable as ToastNotifier() function imported from win10toast.

    toast.show_toast(notifTitle, notifDescription, duration=notifDuration) # Displays a notification using a random title and description from notifTitle and notifDescription and uses the integer collected from notifDuration as the duration for the notification to be displayed for.
    timer.start() # Starts the timer as defined in the timer variable.
    return

notif() # Calls the notif function and sets the notification loop in action.