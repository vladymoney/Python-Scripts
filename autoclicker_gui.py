import pyautogui
import tkinter as tk
from tkinter import ttk
import time
import keyboard

# Global variables to store clicks and running status
clicks = []
is_recording = False
is_running = False

def record_click(event):
    if is_recording:
        x, y = pyautogui.position()
        clicks.append((x, y))
        status_label.config(text=f"Recorded Click: ({x}, {y})")

def start_recording():
    global is_recording, clicks
    is_recording = True
    clicks = []  # Reset previous clicks
    status_label.config(text="Recording clicks...")

def stop_recording():
    global is_recording
    is_recording = False
    status_label.config(text="Stopped recording.")

def start_clicking():
    global is_running
    if not clicks:
        status_label.config(text="No clicks recorded!")
        return

    is_running = True
    interval = float(interval_var.get())
    status_label.config(text="Autoclicking... Press 'Esc' to stop.")
    
    # Click in a loop until stopped
    def click_loop():
        while is_running:
            for x, y in clicks:
                if not is_running:
                    break
                pyautogui.click(x, y)
                time.sleep(interval)
    
    # Start the click loop in a separate thread to not freeze the GUI
    import threading
    threading.Thread(target=click_loop, daemon=True).start()

def stop_clicking():
    global is_running
    is_running = False
    status_label.config(text="Autoclicking stopped.")

# Function to stop clicking when 'Esc' is pressed
keyboard.add_hotkey('esc', stop_clicking)

# Create the GUI
app = tk.Tk()
app.title("Autoclicker")
app.geometry("400x300")

# Interval selection
interval_label = tk.Label(app, text="Interval (seconds):")
interval_label.pack(pady=5)
interval_var = tk.StringVar(value="0.5")
interval_entry = ttk.Entry(app, textvariable=interval_var)
interval_entry.pack(pady=5)

# Buttons
record_button = ttk.Button(app, text="Record", command=start_recording)
record_button.pack(pady=5)
stop_record_button = ttk.Button(app, text="Stop Recording", command=stop_recording)
stop_record_button.pack(pady=5)
start_clicking_button = ttk.Button(app, text="Start Clicking", command=start_clicking)
start_clicking_button.pack(pady=5)
stop_clicking_button = ttk.Button(app, text="Stop Clicking", command=stop_clicking)
stop_clicking_button.pack(pady=5)

# Status label
status_label = tk.Label(app, text="Ready", fg="blue")
status_label.pack(pady=10)

# Bind mouse click events for recording
app.bind("<Button-1>", record_click)

app.mainloop()
