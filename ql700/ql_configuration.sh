#!/bin/bash

# Variables
PRODUCT_ID="04f9"
VENDOR_ID="2042"

# 1. Update the system
echo "Updating system packages..."
sudo apt update
sudo apt upgrade -y

# 2. Install system packages / libraries
echo "Installing required system libraries..."
sudo apt install -y python3 python3-pip python3-venv libusb-1.0-0-dev build-essential gcc

# 3. Give non-root access to the printer
echo "Creating udev rule for Brother QL printer..."
# Use 'tee' to handle sudo redirection safely
echo "SUBSYSTEM==\"usb\", ATTR{idVendor}==\"${VENDOR_ID}\", ATTR{idProduct}==\"${PRODUCT_ID}\", MODE=\"0666\", GROUP=\"lp\"" | sudo tee /etc/udev/rules.d/99-brother-ql.rules > /dev/null

# 4. Reload udev rules
echo "Reloading udev rules..."
sudo udevadm control --reload-rules
sudo udevadm trigger

# 5. Add user to the lp group
echo "Adding current user to the 'lp' group..."
sudo usermod -aG lp $USER

# 6. Apply group changes
echo "Configuration complete. Applying group changes..."
# Note: newgrp starts a new shell. If running as part of a larger automation, 
# a logout/login or reboot is usually preferred to ensure all processes see the group.
newgrp lp