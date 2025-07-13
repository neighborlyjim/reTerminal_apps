# reTerminal Apps

A collection of demo applications for the Seeed reTerminal, featuring touchscreen interaction, hardware sensor integration, and system monitoring.

## Features

### 🖥️ Fullscreen Kiosk Mode
- All applications launch in fullscreen mode for optimal display on the reTerminal
- Press **ESC** key to toggle fullscreen on/off
- Exit buttons provided in each application for easy navigation

### 📱 Applications Included

1. **App Launcher** (`app_launcher.py`)
   - Main menu to launch all demo applications
   - System utilities (Terminal, File Manager)
   - Clean, touch-friendly interface

2. **Touchscreen Demo** (`touchscreen_demo.py`)
   - Interactive touch counting
   - Visual feedback on touch events
   - Background color changing

3. **Hardware Sensors** (`hardware_demo.py`)
   - Real-time accelerometer readings (ST LIS3LV02DL)
   - Light sensor data (LTR-303ALS-01)
   - Based on official Seeed hardware documentation

4. **IoT Dashboard** (`iot_dashboard.py`)
   - System information (CPU, Memory, Disk)
   - Network status and IP address
   - Real-time updates

## Quick Start

### Using the Launch Script
```bash
./launch_apps.sh
```

### Manual Launch
```bash
export DISPLAY=:0
python3 app_launcher.py
```

## Hardware Information

### Screen Configuration
- **Display**: 5-inch capacitive touchscreen (720x1280)
- **Rotation**: 270 degrees (portrait mode)
- **Touch Device**: seeed-tp

### Sensors
- **Light Sensor**: `/sys/bus/iio/devices/iio:device0/in_illuminance_input`
- **Accelerometer**: `/dev/input/event9` (input events)

## Controls

- **ESC**: Toggle fullscreen mode
- **Exit Buttons**: Close individual applications
- **Touch**: All interfaces are touch-optimized

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- psutil (for system monitoring)
- Seeed reTerminal hardware

## Installation

1. Clone this repository:
```bash
git clone https://github.com/neighborlyjim/reTerminal_apps.git
```

2. Make the launch script executable:
```bash
chmod +x launch_apps.sh
```

3. Run the applications:
```bash
./launch_apps.sh
```

## Development

### Display Environment
Applications require `DISPLAY=:0` environment variable for proper display on reTerminal.

### Fullscreen Implementation
All apps use `root.attributes('-fullscreen', True)` for kiosk-style operation.

### Hardware Integration
Sensor readings follow official Seeed documentation paths and methods.

## Troubleshooting

### Display Issues
- Ensure `DISPLAY=:0` is set
- Check Wayfire configuration for proper screen rotation

### Sensor Access
- Verify device permissions for `/dev/input/event9`
- Check IIO device availability at `/sys/bus/iio/devices/`

### Touch Calibration
- Touchscreen should be configured for `seeed-tp` device
- Verify touchscreen alignment with display rotation

## License

MIT License - see individual files for details.

## Links

- [Seeed reTerminal Hardware Documentation](https://wiki.seeedstudio.com/reTerminal-hardware-interfaces-usage/)
- [GitHub Repository](https://github.com/neighborlyjim/reTerminal_apps)
