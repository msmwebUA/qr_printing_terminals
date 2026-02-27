#!/bin/bash

echo "Configuring Waveshare DSI panel in config.txt..."

if ! grep -q "dtoverlay=vc4-kms-dsi-waveshare-panel" /boot/firmware/config.txt; then
    echo "dtoverlay=vc4-kms-dsi-waveshare-panel,10_1_inch,dsi0" | sudo tee -a /boot/firmware/config.txt
fi

# Enable Screen Blanking and set timeout to 300 seconds
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

echo "Touchscreen configuration applied."