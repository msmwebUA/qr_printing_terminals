#!/bin/bash

echo "Set Screen Blanking with timeout..."

sudo apt install -y swayidle wlopm

# Create autostart directory if missing
mkdir -p ~/.config/wayfire.ini.d

# Start idle handler at login
cat > ~/.config/wayfire.ini.d/50-screenblank.conf << 'EOF'
[autostart]
screenblank = swayidle timeout 300 'wlopm --off *' resume 'wlopm --on *'
EOF

echo "Touchscreen configuration applied. Reboot or log out required."