#!/bin/bash

# Define variables
REPO_URL="https://github.com/msmwebUA/qr_printing_terminals.git"
REPO_DIR="qr_printing_terminals_temp"
TARGET_DIR="$HOME/Documents/terminal_app"

echo "Step 1: Cloning the repository..."
# Clone into a temporary directory
git clone "$REPO_URL" "$REPO_DIR"

echo "Step 2: Updating Python files in $TARGET_DIR..."
# Ensure the target directory exists
mkdir -p "$TARGET_DIR"

# Copy all .py files from the repo folder to the target folder
# The 'cp' command with -f will overwrite existing files
cp -f "$REPO_DIR/terminal_app/"*.py "$TARGET_DIR/"

echo "Step 3: Cleaning up..."
# Remove the cloned repository
rm -rf "$REPO_DIR"

echo "Application update successful! All Python files have been replaced by latest version."