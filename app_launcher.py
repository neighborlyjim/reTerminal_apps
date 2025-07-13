#!/usr/bin/env python3
"""
reTerminal App Launcher
Main menu to launch different demo applications
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import os

class AppLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("reTerminal App Launcher")
        # Enable fullscreen mode
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#2c3e50')
        
        # Bind escape key to exit fullscreen
        self.root.bind('<Escape>', self.toggle_fullscreen)
        
        self.app_dir = "/home/jharris/reTerminal_apps"
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="reTerminal Apps", 
                        font=('Arial', 42, 'bold'), 
                        fg='#ecf0f1', bg='#2c3e50')
        title.pack(pady=40)
        
        # Subtitle
        subtitle = tk.Label(self.root, text="Choose an application to launch", 
                           font=('Arial', 20), 
                           fg='#bdc3c7', bg='#2c3e50')
        subtitle.pack(pady=15)
        
        # App buttons frame
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=40, expand=True)
        
        # Define apps
        apps = [
            ("Touchscreen Demo", "touchscreen_demo.py", "#3498db"),
            ("Hardware Sensors", "hardware_demo.py", "#e74c3c"),
            ("IoT Dashboard", "iot_dashboard.py", "#2ecc71"),
        ]
        
        for name, filename, color in apps:
            button = tk.Button(button_frame, 
                              text=name, 
                              font=('Arial', 20, 'bold'),
                              bg=color, fg='white',
                              width=22, height=4,
                              command=lambda f=filename: self.launch_app(f))
            button.pack(pady=25)
            
        # Separator
        separator = tk.Frame(self.root, height=2, bg='#34495e')
        separator.pack(fill='x', padx=50, pady=20)
        
        # System buttons
        system_frame = tk.Frame(self.root, bg='#2c3e50')
        system_frame.pack(pady=40)
        
        # Terminal button
        terminal_btn = tk.Button(system_frame, 
                                text="Open Terminal", 
                                font=('Arial', 18, 'bold'),
                                bg='#95a5a6', fg='white',
                                width=18, height=3,
                                command=self.open_terminal)
        terminal_btn.pack(side=tk.LEFT, padx=20)
        
        # File manager button
        files_btn = tk.Button(system_frame, 
                             text="File Manager", 
                             font=('Arial', 18, 'bold'),
                             bg='#f39c12', fg='white',
                             width=18, height=3,
                             command=self.open_file_manager)
        files_btn.pack(side=tk.LEFT, padx=20)
        
        # Exit button
        exit_button = tk.Button(self.root, 
                               text="Exit Launcher", 
                               font=('Arial', 18, 'bold'),
                               bg='#e74c3c', fg='white',
                               width=20, height=2,
                               command=self.exit_app)
        exit_button.pack(side=tk.BOTTOM, pady=30)
        
    def launch_app(self, filename):
        app_path = os.path.join(self.app_dir, filename)
        try:
            subprocess.Popen(['python3', app_path])
        except Exception as e:
            print(f"Error launching {filename}: {e}")
            
    def open_terminal(self):
        try:
            subprocess.Popen(['x-terminal-emulator'])
        except:
            try:
                subprocess.Popen(['lxterminal'])
            except:
                try:
                    subprocess.Popen(['gnome-terminal'])
                except:
                    print("Could not open terminal")
                    
    def open_file_manager(self):
        try:
            subprocess.Popen(['pcmanfm', self.app_dir])
        except:
            try:
                subprocess.Popen(['nautilus', self.app_dir])
            except:
                print("Could not open file manager")
                
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
    app = AppLauncher(root)
    root.mainloop()
