#!/usr/bin/env python3
"""
reTerminal Hardware Demo
Demonstrates reading from built-in sensors (accelerometer, light sensor, etc.)
"""

import tkinter as tk
from tkinter import ttk
import time
import threading

class HardwareDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("reTerminal Hardware Demo")
        self.root.geometry("720x1280")
        self.root.configure(bg='#34495e')
        
        self.running = True
        # Initialize accelerometer values
        self.accel_x = 0
        self.accel_y = 0
        self.accel_z = 0
        
        self.setup_ui()
        self.start_sensor_thread()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Hardware Sensors", 
                        font=('Arial', 24, 'bold'), 
                        fg='white', bg='#34495e')
        title.pack(pady=20)
        
        # Create frames for different sensors
        self.create_sensor_frame("Accelerometer", "accel")
        self.create_sensor_frame("Light Sensor", "light")
        self.create_sensor_frame("Temperature", "temp")
        
        # Exit button
        exit_button = tk.Button(self.root, 
                               text="Exit", 
                               font=('Arial', 14),
                               bg='#e74c3c', fg='white',
                               width=10, height=1,
                               command=self.close_app)
        exit_button.pack(side=tk.BOTTOM, pady=20)
        
    def create_sensor_frame(self, title, sensor_type):
        frame = tk.Frame(self.root, bg='#2c3e50', relief='raised', bd=2)
        frame.pack(pady=10, padx=20, fill='x')
        
        # Sensor title
        tk.Label(frame, text=title, 
                font=('Arial', 16, 'bold'),
                fg='white', bg='#2c3e50').pack(pady=5)
        
        # Sensor value
        value_label = tk.Label(frame, text="Reading...", 
                              font=('Arial', 14),
                              fg='#ecf0f1', bg='#2c3e50')
        value_label.pack(pady=5)
        
        # Store reference for updates
        setattr(self, f"{sensor_type}_label", value_label)
        
    def read_accelerometer(self):
        try:
            # Read from ST LIS3LV02DL Accelerometer via input device
            import struct
            import os, fcntl
            
            # Open in non-blocking mode
            fd = os.open('/dev/input/event9', os.O_RDONLY | os.O_NONBLOCK)
            
            try:
                # Try to read available data
                for _ in range(5):  # Read up to 5 events
                    try:
                        data = os.read(fd, 24)  # input_event struct size
                        if len(data) == 24:
                            # Parse input_event: sec, usec, type, code, value
                            unpacked = struct.unpack('llHHi', data)
                            event_type, code, value = unpacked[2], unpacked[3], unpacked[4]
                            if event_type == 3:  # EV_ABS (absolute axis)
                                if code == 0:  # X axis
                                    self.accel_x = value
                                elif code == 1:  # Y axis  
                                    self.accel_y = value
                                elif code == 2:  # Z axis
                                    self.accel_z = value
                    except BlockingIOError:
                        break
                    except:
                        break
            finally:
                os.close(fd)
            
            # Return stored values
            return f"X: {self.accel_x}, Y: {self.accel_y}, Z: {self.accel_z}"
        except Exception as e:
            return f"Accelerometer: {str(e)[:20]}..."
            
    def read_light_sensor(self):
        try:
            # Try reading from various possible light sensor paths
            possible_paths = [
                '/sys/class/i2c-dev/i2c-1/device/1-0029/iio:device*/in_illuminance_input',
                '/sys/bus/i2c/devices/1-0029/iio:device*/in_illuminance_input',
                '/proc/device-tree/aliases/light-sensor'
            ]
            
            import glob
            for path_pattern in possible_paths:
                matches = glob.glob(path_pattern)
                for path in matches:
                    try:
                        with open(path, 'r') as f:
                            light = f.read().strip()
                        return f"Light: {light} lux"
                    except:
                        continue
            
            # Fallback: simulate light reading based on time
            import datetime
            hour = datetime.datetime.now().hour
            if 6 <= hour <= 18:
                simulated_light = 300 + (hour - 6) * 50  # Daytime simulation
            else:
                simulated_light = 10  # Nighttime simulation
            return f"Light: ~{simulated_light} lux (simulated)"
        except:
            return "Light sensor: Reading..."
            
    def read_temperature(self):
        try:
            # Read CPU temperature
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                temp_millidegree = int(f.read().strip())
                temp_celsius = temp_millidegree / 1000
            return f"CPU: {temp_celsius:.1f}°C"
        except:
            return "Temperature not available"
    
    def update_sensors(self):
        while self.running:
            try:
                # Update accelerometer
                accel_data = self.read_accelerometer()
                self.root.after(0, lambda: self.accel_label.config(text=accel_data))
                
                # Update light sensor
                light_data = self.read_light_sensor()
                self.root.after(0, lambda: self.light_label.config(text=light_data))
                
                # Update temperature
                temp_data = self.read_temperature()
                self.root.after(0, lambda: self.temp_label.config(text=temp_data))
                
            except Exception as e:
                print(f"Sensor update error: {e}")
                
            time.sleep(1)  # Update every second
    
    def start_sensor_thread(self):
        self.sensor_thread = threading.Thread(target=self.update_sensors, daemon=True)
        self.sensor_thread.start()
        
    def close_app(self):
        self.running = False
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HardwareDemo(root)
    root.mainloop()
