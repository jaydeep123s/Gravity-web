#!/bin/bash

echo "Running tests..."

# Navigate to the app directory
cd app

# Install dependencies
pip3 install -r requirements.txt

# Run a basic test to check if the app starts
python3 -m unittest discover -s tests

echo "Tests completed."
