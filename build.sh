#!/bin/bash

echo "Running tests..."

# Navigate to the app directory
cd app

# Run a basic test to check if the app starts
python3 -m unittest discover -s tests

echo "Tests completed."
