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

echo "Setting timezone to Europe/Helsinki..."

sudo timedatectl set-timezone Europe/Helsinki

echo "Setting WLAN country to Finland (FI)..."

# Set in wpa_supplicant if file exists
if [ -f /etc/wpa_supplicant/wpa_supplicant.conf ]; then
    sudo sed -i '/^country=/d' /etc/wpa_supplicant/wpa_supplicant.conf
    echo "country=FI" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf >/dev/null
fi

# Set via raspi-config if available
if command -v raspi-config >/dev/null 2>&1; then
    sudo raspi-config nonint do_wifi_country FI
fi

# Set in NetworkManager if present
if [ -d /etc/NetworkManager/conf.d ]; then
    sudo mkdir -p /etc/NetworkManager/conf.d
    cat <<EOF | sudo tee /etc/NetworkManager/conf.d/wifi-country.conf >/dev/null
[device]
wifi.scan-rand-mac-address=no

[connection]
wifi.country=FI
EOF
    sudo systemctl restart NetworkManager || true
fi

echo "Touchscreen configuration applied. Reboot or log out required."