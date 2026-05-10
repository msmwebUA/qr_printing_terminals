#!/bin/bash

echo "Setting timezone to Europe/Helsinki..."

sudo timedatectl set-timezone Europe/Helsinki
echo "Europe/Helsinki" | sudo tee /etc/timezone
sudo ln -sf /usr/share/zoneinfo/Europe/Helsinki /etc/localtime

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

echo "Touchscreen configuration applied. Reboot or logout required."