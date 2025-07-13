#!/bin/bash
# reTerminal Apps Launcher Script
# Launches fullscreen app launcher for kiosk-style operation

echo "Starting reTerminal Apps in fullscreen mode..."
echo "Press ESC to toggle fullscreen on/off"
echo "Use Exit buttons to close applications"

# Set display environment
export DISPLAY=:0

# Change to app directory
cd /home/jharris/reTerminal_apps

# Launch the app launcher
python3 app_launcher.py
