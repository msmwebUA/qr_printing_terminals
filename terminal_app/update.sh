#!/bin/bash

# Define paths
UPDATE_SCRIPT_URL="https://raw.githubusercontent.com/msmwebUA/qr_printing_terminals/refs/heads/main/terminal_app/latest_update_script.sh"
TARGET_DIR="$HOME/Documents/terminal_app"
SCRIPT_NAME="latest_update_script.sh"

echo "Step 1: Downloading the latest update script..."
# Ensure target directory exists
mkdir -p "$TARGET_DIR"

# Download the script using curl
curl -L "$UPDATE_SCRIPT_URL" -o "$TARGET_DIR/$SCRIPT_NAME"

echo "Step 2: Executing the update script..."
# Make it executable and run it
chmod +x "$TARGET_DIR/$SCRIPT_NAME"
cd "$TARGET_DIR" && ./"$SCRIPT_NAME"

echo "Step 3: Cleaning up..."
# Delete the temporary update script
rm "$TARGET_DIR/$SCRIPT_NAME"

echo "Update process finished."