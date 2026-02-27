#!/bin/bash

# 1. Enable SPI interface in Raspberry Pi configuration
echo "Enabling SPI interface..."
# Using raspi-config non-interactive command to enable SPI
sudo raspi-config nonint do_spi 0

# Also ensure the SPI overlay is in /boot/firmware/config.txt (Trixie path)
if ! grep -q "^dtparam=spi=on" /boot/firmware/config.txt; then
    echo "Adding dtparam=spi=on to /boot/firmware/config.txt"
    echo "dtparam=spi=on" | sudo tee -a /boot/firmware/config.txt
fi

# 2. Install system dependencies
echo "Installing lgpio dependencies..."
# Raspberry Pi 5 requires lgpio as the older RPi.GPIO is deprecated for hardware access
# sudo apt update
sudo apt install -y python3-lgpio liblgpio-dev

echo "SPI configuration finished. A reboot is recommended for all changes to take effect."
