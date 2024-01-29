#!/bin/bash

# Script to set up a Python virtual environment and install dependencies

# Name of the virtual environment
VENV_NAME="venv"

# Check if the virtual environment already exists
if [ -d "$VENV_NAME" ]; then
  echo "Virtual environment $VENV_NAME already exists. Activating it."
  source $VENV_NAME/bin/activate
else
  # Create the virtual environment
  echo "Creating virtual environment named $VENV_NAME."
  python3 -m venv $VENV_NAME

  # Activate the virtual environment
  echo "Activating the virtual environment."
  source $VENV_NAME/bin/activate

  # Check if requirements.txt exists
  if [ -f "requirements.txt" ]; then
    # Install dependencies from requirements.txt
    echo "Installing dependencies from requirements.txt."
    pip install -r requirements.txt
  else
    echo "requirements.txt not found. Skipping dependency installation."
  fi
fi

echo "Virtual environment setup and activation complete."
