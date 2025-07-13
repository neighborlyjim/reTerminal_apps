#!/usr/bin/env python3
"""
Simple Touchscreen Demo for reTerminal
This app demonstrates basic touchscreen interaction
"""

import tkinter as tk
from tkinter import ttk
import time

class TouchscreenDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("reTerminal Touchscreen Demo")
        # Enable fullscreen mode
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#2c3e50')
        
        # Bind escape key to exit fullscreen
        self.root.bind('<Escape>', self.toggle_fullscreen)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="reTerminal Demo", 
                        font=('Arial', 24, 'bold'), 
                        fg='white', bg='#2c3e50')
        title.pack(pady=20)
        
        # Touch counter
        self.touch_count = 0
        self.counter_label = tk.Label(self.root, 
                                     text=f"Touch Count: {self.touch_count}",
                                     font=('Arial', 18),
                                     fg='white', bg='#2c3e50')
        self.counter_label.pack(pady=10)
        
        # Large touch button
        self.touch_button = tk.Button(self.root, 
                                     text="Touch Me!", 
                                     font=('Arial', 20, 'bold'),
                                     bg='#3498db', fg='white',
                                     width=15, height=3,
                                     command=self.on_touch)
        self.touch_button.pack(pady=30)
        
        # Color change button
        color_button = tk.Button(self.root, 
                                text="Change Color", 
                                font=('Arial', 16),
                                bg='#e74c3c', fg='white',
                                width=15, height=2,
                                command=self.change_color)
        color_button.pack(pady=20)
        
        # Status display
        self.status_label = tk.Label(self.root, 
                                    text="Ready for touch input",
                                    font=('Arial', 14),
                                    fg='#ecf0f1', bg='#2c3e50')
        self.status_label.pack(pady=20)
        
        # Exit button
        exit_button = tk.Button(self.root, 
                               text="Exit", 
                               font=('Arial', 14),
                               bg='#95a5a6', fg='white',
                               width=10, height=1,
                               command=self.exit_app)
        exit_button.pack(side=tk.BOTTOM, pady=20)
        
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
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)
        
    def exit_app(self):
        """Exit the application"""
        self.root.quit()
        self.root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TouchscreenDemo(root)
    root.mainloop()
