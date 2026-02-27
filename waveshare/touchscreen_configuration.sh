#!/bin/bash

# 1. Add line to the RPI Config File
echo "Configuring Waveshare DSI panel in config.txt..."
# We target /boot/firmware/config.txt which is standard for Trixie/Bookworm
if ! grep -q "dtoverlay=vc4-kms-dsi-waveshare-panel" /boot/firmware/config.txt; then
    echo "dtoverlay=vc4-kms-dsi-waveshare-panel,10_1_inch,dsi0" | sudo tee -a /boot/firmware/config.txt
fi

# 2. Enable Screen Blanking and set timeout to 300 seconds
echo "Configuring screen blanking in labwc autostart..."
AUTOSTART_FILE="$HOME/.config/labwc/autostart"
mkdir -p "$(dirname "$AUTOSTART_FILE")"

# If the file doesn't exist, create it. If it does, update or add the timeout.
if [ -f "$AUTOSTART_FILE" ]; then
    if grep -q "swayidle" "$AUTOSTART_FILE"; then
        # Update existing swayidle/timeout line if present
        sed -i 's/timeout [0-9]*/timeout 300/g' "$AUTOSTART_FILE"
    else
        echo "swayidle -w timeout 300 'wlopm --off *' resume 'wlopm --on *' &" >> "$AUTOSTART_FILE"
    fi
else
    echo "swayidle -w timeout 300 'wlopm --off *' resume 'wlopm --on *' &" > "$AUTOSTART_FILE"
fi

# 3. Set Brightness to 40%
echo "Setting brightness to 40%..."
# On RPi 5, brightness is usually controlled via sysfs
# 40% of 255 is roughly 102
if [ -d "/sys/class/backlight/10-0045" ]; then
    echo 102 | sudo tee /sys/class/backlight/10-0045/brightness
elif [ -d "/sys/class/backlight/4-0045" ]; then
    echo 102 | sudo tee /sys/class/backlight/4-0045/brightness
fi

# 4. Enable Single Click to open directories in file manager
echo "Setting file manager to single-click mode..."
# Update libfm.conf
sed -i 's/single_click=0/single_click=1/g' ~/.config/libfm/libfm.conf

echo "Touchscreen configuration applied."

echo "Remember to set screen mode to Multitouch manually after reboot."