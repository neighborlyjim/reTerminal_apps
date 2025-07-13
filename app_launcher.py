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
        # Set explicit geometry for fullscreen
        self.root.geometry("1280x720")  # reTerminal screen size
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#2c3e50')
        
        # Remove window decorations
        self.root.overrideredirect(True)
        
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
        button_frame.pack(pady=20, expand=True)
        
        # Define apps
        apps = [
            ("Touchscreen Demo", "touchscreen_demo.py", "#3498db"),
            ("Hardware Sensors", "hardware_demo.py", "#e74c3c"),
            ("IoT Dashboard", "iot_dashboard.py", "#2ecc71"),
        ]
        
        # Adjust button layout to two columns
        left_column = tk.Frame(button_frame, bg='#2c3e50')
        left_column.pack(side=tk.LEFT, padx=20)
        right_column = tk.Frame(button_frame, bg='#2c3e50')
        right_column.pack(side=tk.LEFT, padx=20)

        for i, (name, filename, color) in enumerate(apps):
            column = left_column if i % 2 == 0 else right_column
            button = tk.Button(column, 
                              text=name, 
                              font=('Arial', 18, 'bold'),
                              bg=color, fg='white',
                              width=20, height=3,
                              command=lambda f=filename: self.launch_app(f))
            button.pack(pady=15)

        # Add File Manager button to the second column
        files_btn = tk.Button(right_column, 
                             text="File Manager", 
                             font=('Arial', 16, 'bold'),
                             bg='#f39c12', fg='white',
                             width=20, height=3,
                             command=self.open_file_manager)
        files_btn.pack(pady=15)
            
        # Separator
        separator = tk.Frame(self.root, height=2, bg='#34495e')
        separator.pack(fill='x', padx=50, pady=10)
        
        # System buttons
        system_frame = tk.Frame(self.root, bg='#2c3e50')
        system_frame.pack(pady=20)
        
        # Terminal button
        terminal_btn = tk.Button(system_frame, 
                                text="Open Terminal", 
                                font=('Arial', 16, 'bold'),
                                bg='#95a5a6', fg='white',
                                width=20, height=3,
                                command=self.open_terminal)
        terminal_btn.pack(side=tk.LEFT, padx=10)
        
        # Exit button
        exit_button = tk.Button(self.root, 
                               text="Exit Launcher", 
                               font=('Arial', 18, 'bold'),
                               bg='#e74c3c', fg='white',
                               width=20, height=2,
                               command=self.exit_app)
        exit_button.pack(side=tk.BOTTOM, pady=20)
        
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
        # Toggle overrideredirect to show/hide window decorations
        current_override = self.root.overrideredirect()
        self.root.overrideredirect(not current_override)
        if not current_override:
            self.root.geometry("1280x720")
        
    def exit_app(self):
        """Exit the application"""
        self.root.quit()
        self.root.destroy()
        os.system("pkill -f python3")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppLauncher(root)
    root.mainloop()
