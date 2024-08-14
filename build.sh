#!/bin/bash

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Run unit tests
python -m unittest discover -s app/tests

# Deactivate the virtual environment
deactivate
