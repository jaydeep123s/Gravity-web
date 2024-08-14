#!/bin/bash

echo "Deploying application..."

# Navigate to the app directory
cd app

# Start the Flask application
nohup python app.py > /dev/null 2>&1 &

echo "Deployment completed."
