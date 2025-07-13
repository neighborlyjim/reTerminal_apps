#!/usr/bin/env python3
"""
Main Dashboard for reTerminal
Allows navigation between IoT Dashboard, Hardware Demo, and Touchscreen Demo
"""

import tkinter as tk
import subprocess
import os

class MainDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("reTerminal Main Dashboard")
        self.root.geometry("1280x720")  # reTerminal screen size
        self.root.configure(bg='#1a252f')

        # Remove window decorations
        self.root.overrideredirect(True)

        # Bind escape key to exit fullscreen
        self.root.bind('<Escape>', self.close_app)

        self.setup_ui()

    def setup_ui(self):
        # Main title
        title = tk.Label(self.root, text="Main Dashboard", 
                        font=('Arial', 36, 'bold'), 
                        fg='#00d4aa', bg='#1a252f')
        title.pack(pady=30)

        # Buttons for launching apps
        tk.Button(self.root, text="IoT Dashboard", 
                  font=('Arial', 18, 'bold'), 
                  bg='#00d4aa', fg='white', 
                  width=20, height=2, 
                  command=self.launch_iot_dashboard).pack(pady=20)

        tk.Button(self.root, text="Hardware Demo", 
                  font=('Arial', 18, 'bold'), 
                  bg='#00d4aa', fg='white', 
                  width=20, height=2, 
                  command=self.launch_hardware_demo).pack(pady=20)

        tk.Button(self.root, text="Touchscreen Demo", 
                  font=('Arial', 18, 'bold'), 
                  bg='#00d4aa', fg='white', 
                  width=20, height=2, 
                  command=self.launch_touchscreen_demo).pack(pady=20)

        # Exit button
        tk.Button(self.root, text="Exit Dashboard", 
                  font=('Arial', 18, 'bold'), 
                  bg='#ff6b6b', fg='white', 
                  width=20, height=2, 
                  command=self.close_app).pack(pady=30)

    def launch_iot_dashboard(self):
        subprocess.Popen(["python3", "iot_dashboard.py"], cwd=os.path.dirname(__file__))

    def launch_hardware_demo(self):
        subprocess.Popen(["python3", "hardware_demo.py"], cwd=os.path.dirname(__file__))

    def launch_touchscreen_demo(self):
        subprocess.Popen(["python3", "touchscreen_demo.py"], cwd=os.path.dirname(__file__))

    def close_app(self):
        self.root.quit()
        self.root.destroy()
        os.system("pkill -f python3")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainDashboard(root)
    root.mainloop()
