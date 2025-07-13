#!/usr/bin/env python3
"""
Simple Touchscreen Demo for reTerminal
This app demonstrates basic touchscreen interaction
"""

import tkinter as tk
from tkinter import ttk
import time
import subprocess

class TouchscreenDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("reTerminal Touchscreen Demo")
        # Set explicit geometry for fullscreen
        self.root.geometry("1280x720")  # reTerminal screen size
        # Temporarily disable fullscreen mode for debugging
        # self.root.attributes('-fullscreen', True)
        # self.root.overrideredirect(True)
        
        # Bind escape key to exit fullscreen
        self.root.bind('<Escape>', self.toggle_fullscreen)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="reTerminal Demo", 
                        font=('Arial', 36, 'bold'), 
                        fg='white', bg='#2c3e50')
        title.pack(pady=40)
        
        # Touch counter
        self.touch_count = 0
        self.counter_label = tk.Label(self.root, 
                                     text=f"Touch Count: {self.touch_count}",
                                     font=('Arial', 24),
                                     fg='white', bg='#2c3e50')
        self.counter_label.pack(pady=20)
        
        # Large touch button
        self.touch_button = tk.Button(self.root, 
                                     text="Touch Me!", 
                                     font=('Arial', 28, 'bold'),
                                     bg='#3498db', fg='white',
                                     width=20, height=6,
                                     command=self.on_touch)
        self.touch_button.pack(pady=50)
        
        # Color change button
        color_button = tk.Button(self.root, 
                                text="Change Color", 
                                font=('Arial', 20, 'bold'),
                                bg='#e74c3c', fg='white',
                                width=18, height=3,
                                command=self.change_color)
        color_button.pack(pady=30)
        
        # Status display
        self.status_label = tk.Label(self.root, 
                                    text="Ready for touch input",
                                    font=('Arial', 18),
                                    fg='#ecf0f1', bg='#2c3e50')
        self.status_label.pack(pady=30)
        
        # Exit button
        exit_button = tk.Button(self.root, 
                               text="Exit", 
                               font=('Arial', 18, 'bold'),
                               bg='#95a5a6', fg='white',
                               width=15, height=2,
                               command=self.exit_app)
        exit_button.pack(side=tk.BOTTOM, pady=20)
        
        # Add back button
        back_button = tk.Button(self.root, 
                               text="Back to Launcher", 
                               font=('Arial', 18, 'bold'),
                               bg='#3498db', fg='white',
                               width=18, height=2,
                               command=self.back_to_launcher)
        back_button.pack(side=tk.BOTTOM, pady=30)
        
    def on_touch(self):
        self.touch_count += 1
        self.counter_label.config(text=f"Touch Count: {self.touch_count}")
        self.status_label.config(text=f"Button touched at {time.strftime('%H:%M:%S')}")
        
        # Visual feedback
        self.touch_button.config(bg='#2ecc71')
        self.root.after(200, lambda: self.touch_button.config(bg='#3498db'))
        
    def change_color(self):
        colors = ['#2c3e50', '#34495e', '#8e44ad', '#16a085', '#f39c12']
        import random
        new_color = random.choice(colors)
        self.root.config(bg=new_color)
        self.counter_label.config(bg=new_color)
        self.status_label.config(bg=new_color)
        
    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode (Escape key)"""
        # Toggle overrideredirect to show/hide window decorations
        current_override = self.root.overrideredirect()
        self.root.overrideredirect(not current_override)
        if not current_override:
            self.root.geometry("1280x720")
        
    def exit_app(self):
        """Exit the application"""
        self.root.quit()
        self.root.destroy()
        
    def back_to_launcher(self):
        self.running = False
        self.root.quit()
        self.root.destroy()
        subprocess.Popen(['python3', 'app_launcher.py'])
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TouchscreenDemo(root)
    root.mainloop()
