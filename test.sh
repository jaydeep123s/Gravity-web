#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the tests
python -m unittest discover -s app/tests

# Deactivate the virtual environment
deactivate
