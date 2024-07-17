#!/bin/bash

# Define log file path
logFile="build_log.txt"

# Function to write log messages
function write_log {
    timestamp=$(date +"%d-%m-%Y %T")
    echo "$timestamp - $1" >> "$logFile"
}

# Remove previous build and dist directories
write_log "Removing previous build and dist directories"
rm -rf dist
rm -rf build

# Get the Python installation directory
write_log "Getting Python installation directory"
PYTHON_DIR=$(python py_to_exe.py | tr -d '\r')

# Run the py_to_exe.py script to generate the PyInstaller spec file
write_log "Running py_to_exe.py to generate spec file"
"$PYTHON_DIR/python.exe" python_src/py_to_exe.py

# Run PyInstaller with the generated spec file
write_log "Running PyInstaller with generated spec file"
pyinstaller python_src/NovaDireita.spec

# Display completion message and log it
echo "Build process completed."
write_log "Build process completed."