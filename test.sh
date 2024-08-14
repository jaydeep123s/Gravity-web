#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run tests
python -m unittest discover -s app/tests
