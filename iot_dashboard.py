#!/usr/bin/env python3
"""
Simple IoT Dashboard for reTerminal
Displays system information and network status
"""

import tkinter as tk
from tkinter import ttk
import psutil
import time
import threading
import subprocess

class IoTDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("reTerminal IoT Dashboard")
        # Set explicit geometry for fullscreen
        self.root.geometry("1280x720")  # reTerminal screen size
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#1a252f')
        
        # Remove window decorations
        self.root.overrideredirect(True)
        
        # Bind escape key to exit fullscreen
        self.root.bind('<Escape>', self.toggle_fullscreen)
        
        self.running = True
        self.setup_ui()
        self.start_update_thread()
        
    def setup_ui(self):
        # Main title
        title = tk.Label(self.root, text="IoT Dashboard", 
                        font=('Arial', 36, 'bold'), 
                        fg='#00d4aa', bg='#1a252f')
        title.pack(pady=30)
        
        # System info frame
        self.create_info_frame()
        
        # Network frame
        self.create_network_frame()
        
        # Resource usage frame
        self.create_resource_frame()
        
        # Exit button
        exit_button = tk.Button(self.root, 
                               text="Exit Dashboard", 
                               font=('Arial', 18, 'bold'),
                               bg='#ff6b6b', fg='white',
                               width=18, height=2,
                               command=self.close_app)
        exit_button.pack(side=tk.BOTTOM, pady=30)
        
        # Add back button
        back_button = tk.Button(self.root, 
                               text="Back to Launcher", 
                               font=('Arial', 18, 'bold'),
                               bg='#3498db', fg='white',
                               width=18, height=2,
                               command=self.back_to_launcher)
        back_button.pack(side=tk.BOTTOM, pady=30)
        
    def create_info_frame(self):
        frame = tk.LabelFrame(self.root, text="System Information", 
                             font=('Arial', 18, 'bold'),
                             fg='#00d4aa', bg='#1a252f', 
                             labelanchor='n')
        frame.pack(pady=15, padx=30, fill='x')
        
        # Hostname
        self.hostname_label = tk.Label(frame, text="Hostname: Loading...", 
                                      font=('Arial', 16),
                                      fg='white', bg='#1a252f')
        self.hostname_label.pack(anchor='w', padx=15, pady=5)
        
        # Uptime
        self.uptime_label = tk.Label(frame, text="Uptime: Loading...", 
                                    font=('Arial', 16),
                                    fg='white', bg='#1a252f')
        self.uptime_label.pack(anchor='w', padx=15, pady=5)
        
        # Current time
        self.time_label = tk.Label(frame, text="Time: Loading...", 
                                  font=('Arial', 16),
                                  fg='white', bg='#1a252f')
        self.time_label.pack(anchor='w', padx=15, pady=5)
        
    def create_network_frame(self):
        frame = tk.LabelFrame(self.root, text="Network Status", 
                             font=('Arial', 18, 'bold'),
                             fg='#00d4aa', bg='#1a252f',
                             labelanchor='n')
        frame.pack(pady=15, padx=30, fill='x')
        
        # IP Address
        self.ip_label = tk.Label(frame, text="IP Address: Loading...", 
                                font=('Arial', 12),
                                fg='white', bg='#1a252f')
        self.ip_label.pack(anchor='w', padx=10, pady=2)
        
        # WiFi Status
        self.wifi_label = tk.Label(frame, text="WiFi: Loading...", 
                                  font=('Arial', 12),
                                  fg='white', bg='#1a252f')
        self.wifi_label.pack(anchor='w', padx=10, pady=2)
        
    def create_resource_frame(self):
        frame = tk.LabelFrame(self.root, text="Resource Usage", 
                             font=('Arial', 18, 'bold'),
                             fg='#00d4aa', bg='#1a252f',
                             labelanchor='n')
        frame.pack(pady=15, padx=30, fill='x')
        
        # CPU Usage
        self.cpu_label = tk.Label(frame, text="CPU: Loading...", 
                                 font=('Arial', 16),
                                 fg='white', bg='#1a252f')
        self.cpu_label.pack(anchor='w', padx=15, pady=5)
        
        # Memory Usage
        self.memory_label = tk.Label(frame, text="Memory: Loading...", 
                                    font=('Arial', 16),
                                    fg='white', bg='#1a252f')
        self.memory_label.pack(anchor='w', padx=15, pady=5)
        
        # Disk Usage
        self.disk_label = tk.Label(frame, text="Disk: Loading...", 
                                  font=('Arial', 16),
                                  fg='white', bg='#1a252f')
        self.disk_label.pack(anchor='w', padx=10, pady=2)
        
        # Temperature
        self.temp_label = tk.Label(frame, text="Temperature: Loading...", 
                                  font=('Arial', 12),
                                  fg='white', bg='#1a252f')
        self.temp_label.pack(anchor='w', padx=10, pady=2)
        
    def get_ip_address(self):
        try:
            result = subprocess.run(['hostname', '-I'], 
                                  capture_output=True, text=True)
            return result.stdout.strip().split()[0] if result.stdout.strip() else "Not connected"
        except:
            return "Unknown"
            
    def get_wifi_status(self):
        try:
            result = subprocess.run(['iwconfig'], 
                                  capture_output=True, text=True, 
                                  stderr=subprocess.DEVNULL)
            if 'ESSID:' in result.stdout:
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'ESSID:' in line:
                        essid = line.split('ESSID:')[1].strip().strip('"')
                        return f"Connected to {essid}" if essid != "off/any" else "Not connected"
            return "Not connected"
        except:
            return "Unknown"
    
    def update_dashboard(self):
        while self.running:
            try:
                # Update hostname
                hostname = subprocess.run(['hostname'], 
                                        capture_output=True, text=True).stdout.strip()
                self.root.after(0, lambda: self.hostname_label.config(
                    text=f"Hostname: {hostname}"))
                
                # Update uptime
                uptime = time.time() - psutil.boot_time()
                hours = int(uptime // 3600)
                minutes = int((uptime % 3600) // 60)
                self.root.after(0, lambda: self.uptime_label.config(
                    text=f"Uptime: {hours}h {minutes}m"))
                
                # Update current time
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                self.root.after(0, lambda: self.time_label.config(
                    text=f"Time: {current_time}"))
                
                # Update IP address
                ip_addr = self.get_ip_address()
                self.root.after(0, lambda: self.ip_label.config(
                    text=f"IP Address: {ip_addr}"))
                
                # Update WiFi status
                wifi_status = self.get_wifi_status()
                self.root.after(0, lambda: self.wifi_label.config(
                    text=f"WiFi: {wifi_status}"))
                
                # Update CPU usage
                cpu_percent = psutil.cpu_percent(interval=1)
                self.root.after(0, lambda: self.cpu_label.config(
                    text=f"CPU: {cpu_percent:.1f}%"))
                
                # Update memory usage
                memory = psutil.virtual_memory()
                self.root.after(0, lambda: self.memory_label.config(
                    text=f"Memory: {memory.percent:.1f}% ({memory.used//1024//1024}MB used)"))
                
                # Update disk usage
                disk = psutil.disk_usage('/')
                disk_percent = (disk.used / disk.total) * 100
                self.root.after(0, lambda: self.disk_label.config(
                    text=f"Disk: {disk_percent:.1f}% ({disk.used//1024//1024//1024}GB used)"))
                
                # Update temperature
                try:
                    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                        temp = int(f.read().strip()) / 1000
                    self.root.after(0, lambda: self.temp_label.config(
                        text=f"Temperature: {temp:.1f}°C"))
                except:
                    self.root.after(0, lambda: self.temp_label.config(
                        text="Temperature: N/A"))
                
            except Exception as e:
                print(f"Dashboard update error: {e}")
                
            time.sleep(2)  # Update every 2 seconds
    
    def start_update_thread(self):
        self.update_thread = threading.Thread(target=self.update_dashboard, daemon=True)
        self.update_thread.start()
        
    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode (Escape key)"""
        # Toggle overrideredirect to show/hide window decorations
        current_override = self.root.overrideredirect()
        self.root.overrideredirect(not current_override)
        if not current_override:
            self.root.geometry("1280x720")
        
    def close_app(self):
        self.running = False
        self.root.quit()
        self.root.destroy()
        
    def back_to_launcher(self):
        self.running = False
        self.root.quit()
        self.root.destroy()
        subprocess.Popen(['python3', 'app_launcher.py'])

if __name__ == "__main__":
    root = tk.Tk()
    app = IoTDashboard(root)
    root.mainloop()
