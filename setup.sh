#!/bin/bash

# Start logging
LOG_FILE="$HOME/Documents/setup_log.txt"
exec > >(tee -i "$LOG_FILE") 2>&1

echo "=========================================="
echo "STARTING TERMINAL SETUP: $(date)"
echo "=========================================="

# Define paths
REPO_URL="https://github.com/msmwebUA/qr_printing_terminals.git"
REPO_DIR="qr_printing_terminals"
TARGET_DIR="$HOME/Documents/terminal_app"
VENV_PATH="$HOME/Documents/venv"

echo "--- Updating system packages ---"
sudo apt update
# sudo apt upgrade -y

echo "--- Cloning application repository ---"
git clone $REPO_URL

echo "--- Hardware configuration ---"
# Make scripts executable and run them
chmod +x $REPO_DIR/rc522/rc_configuration.sh
chmod +x $REPO_DIR/ql700/ql_configuration.sh
chmod +x $REPO_DIR/waveshare/touchscreen_configuration.sh

./$REPO_DIR/rc522/rc_configuration.sh
./$REPO_DIR/ql700/ql_configuration.sh
./$REPO_DIR/waveshare/touchscreen_configuration.sh

echo "--- Moving application files ---"
# Create target directory
mkdir -p $TARGET_DIR

FILES=("app.py" "config.py" "database.py" "label.py" "main.py" "print_label.py" "resources_rc.py" "scan_card.py" "ui.py" "update.sh")
for file in "${FILES[@]}"; do
    mv "$REPO_DIR/terminal_app/$file" "$TARGET_DIR/"
done
# Make update script executable
chmod +x $TARGET_DIR/update.sh

echo "--- Setting up Python Virtual Environment ---"
rm -rf $VENV_PATH
python3 -m venv $VENV_PATH
"$VENV_PATH/bin/pip" install --upgrade pip
"$VENV_PATH/bin/pip" install -r "$REPO_DIR/terminal_app/requirements/requirements.txt"

echo "--- Creating startup script start_app.sh ---"
cat <<EOF > "$TARGET_DIR/start_app.sh"
#!/bin/bash
VENV_PATH="\$HOME/Documents/venv/bin/activate"
APP_PATH="\$HOME/Documents/terminal_app/main.py"
source "\$VENV_PATH" && python3 "\$APP_PATH"
EOF
chmod +x "$TARGET_DIR/start_app.sh"

echo "--- Install emoji font ---"
sudo apt install -y fonts-noto-color-emoji

echo "--- Cleanup ---"
rm -rf $REPO_DIR

echo "################
1. Remember to set touchscreen after reboot:
1.1 Set brightness and turn on Multitouch Mode

Menu → Preferences → Control Centre → Screens → Screens → DSI-1 → Brightness
DSI-1 → Touchscreen → Mode (for multitouch configuration)
Also enable **10-0014 Goodix Touchscreen** (or your touchscreen name) in the same Touchscreen Menu

1.2 Enable Single Click in File Manager to open directories

2. After reboot, consider to upgrade all system packages with command:
sudo apt upgrade
################"

read -p "Your terminal application is installed in $TARGET_DIR. Reboot required. Do you want to reboot now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    sudo reboot
fi