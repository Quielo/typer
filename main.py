import tkinter as tk
from threading import Thread
import pyautogui
import random
import time

class TypingApp:
    def __init__(self, master):
        self.master = master
        master.geometry("250x300")  # Adjust the window size if needed

        self.state = False  # False means stopped, True means running

        # Notification area
        self.notification_area = tk.Label(master, text="", height=4)
        self.notification_area.pack(fill=tk.X, padx=20, pady=5)

        # Create frames for each button to control size more precisely
        self.start_frame = tk.Frame(master, width=150, height=75)
        self.start_frame.pack_propagate(False)  # Prevent frame from resizing to fit the button
        self.start_frame.pack(padx=20, pady=10)
        self.start_button = tk.Button(self.start_frame, text="Start", command=self.start_typing)
        self.start_button.pack(fill=tk.BOTH, expand=True)

        self.stop_frame = tk.Frame(master, width=150, height=75)
        self.stop_frame.pack_propagate(False)  # Prevent frame from resizing to fit the button
        self.stop_frame.pack(padx=20, pady=10)
        self.stop_button = tk.Button(self.stop_frame, text="Stop", command=self.stop_typing)
        self.stop_button.pack(fill=tk.BOTH, expand=True)

    def update_notification(self, message):
        # Update the notification label with the provided message
        self.notification_area.config(text=message)

    def typing_action(self):
        #self.update_notification("The program will start typing in 10sec.")
        #time.sleep(10)  # Wait for 10 seconds before starting
        if self.state:  # Check if still in running state after wait
            while self.state:
                letter = random.choice('abcd efgh ijkl mnop qrst uvw xyz')  # Select a random letter
                pyautogui.typewrite(letter)  # Type the letter
                delay = random.randint(1, 5)  # Random delay between 1 and 5 seconds
                time.sleep(delay)

    def start_typing(self):
        if not self.state:
            self.state = True
            # Update notification on main thread
            self.master.after(0, self.update_notification, "Starting soon...")
            t = Thread(target=self.typing_action)
            t.start()

    def stop_typing(self):
        self.state = False
        # Update notification on the main thread to ensure it pops up immediately
        self.master.after(0, self.update_notification, "The program was stopped.")

root = tk.Tk()
app = TypingApp(root)
root.mainloop()
