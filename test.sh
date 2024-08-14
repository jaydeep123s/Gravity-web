#!/bin/bash

echo "Running tests..."

# Navigate to the app directory
cd app

# Install dependencies
pip3 install -r requirements.txt

# Run the tests
python3 -m unittest discover -s tests

echo "Tests completed."
