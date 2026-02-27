#!/bin/bash

# Define variables
REPO_URL="https://github.com/msmwebUA/qr_printing_terminals.git"
REPO_DIR="qr_printing_terminals_temp"
TARGET_DIR="$HOME/Documents/terminal_app"
VENV_PATH="$HOME/Documents/venv/bin/activate"

echo "Step 1: Cloning the repository..."
# Clone into a temporary directory
git clone "$REPO_URL" "$REPO_DIR"

echo "Step 2: Updating Python files in $TARGET_DIR..."
# Ensure the target directory exists
mkdir -p "$TARGET_DIR"

# Copy all .py files from the repo folder to the target folder
# The 'cp' command with -f will overwrite existing files
cp -f "$REPO_DIR/terminal_app/"*.py "$TARGET_DIR/"

echo "Step 3: Installing/Updating libraries from requirements.txt..."
# Check if venv exists before activating
if [ -f "$VENV_PATH" ]; then
    source "$VENV_PATH"
    pip install --upgrade pip
    pip install -r "$REPO_DIR/terminal_app/requirenments.txt"
else
    echo "Warning: Virtual environment not found at $VENV_PATH. Skipping library installation."
fi

echo "Step 4: Cleaning up..."
rm -rf "$REPO_DIR"

echo "Update successful! Python files and libraries are up to date."