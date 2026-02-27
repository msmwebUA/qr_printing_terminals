#!/bin/bash

# Define paths
REPO_URL="https://github.com/msmwebUA/qr_printing_terminals.git"
REPO_DIR="qr_printing_terminals"
TARGET_DIR="$HOME/Documents/terminal_app"
VENV_PATH="$HOME/Documents/venv"

echo "--- Step 1: Cloning repository ---"
git clone $REPO_URL

# Create target directory
mkdir -p $TARGET_DIR

echo "--- Moving application files ---"
FILES=("app.py" "config.py" "database.py" "label.py" "main.py" "print_label.py" "resources_rc.py" "scan_card.py" "ui.py" "update.sh")
for file in "${FILES[@]}"; do
    mv "$REPO_DIR/terminal_app/$file" "$TARGET_DIR/"
done

echo "--- Setting up Python Virtual Environment ---"
rm -rf $VENV_PATH
python3 -m venv $VENV_PATH
source "$VENV_PATH/bin/activate"
pip install --upgrade pip
pip install -r "$REPO_DIR/terminal_app/requirements/requirements.txt"

echo "--- Creating startup script start_app.sh ---"
cat <<EOF > "$TARGET_DIR/start_app.sh"
#!/bin/bash
VENV_PATH="\$HOME/Documents/venv/bin/activate"
APP_PATH="\$HOME/Documents/terminal_app/main.py"
source "\$VENV_PATH" && python3 "\$APP_PATH"
EOF
chmod +x "$TARGET_DIR/start_app.sh"

echo "--- Hardware configuration ---"
# Make scripts executable and run them
chmod +x $REPO_DIR/waveshare/touchscreen_configuration.sh
chmod +x $REPO_DIR/rc522/rc_configuration.sh
chmod +x $REPO_DIR/ql700/ql_configuration.sh

./$REPO_DIR/waveshare/touchscreen_configuration.sh
./$REPO_DIR/rc522/rc_configuration.sh
./$REPO_DIR/ql700/ql_configuration.sh

echo "--- Cleanup ---"
rm -rf $REPO_DIR

echo "Your terminal is configured in $TARGET_DIR"

read -p "Reboot required. Do you want to reboot now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    sudo reboot
fi