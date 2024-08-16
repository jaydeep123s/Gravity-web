#!/bin/bash

# Print a message indicating the start of the deployment
echo "Starting deployment..."

# Navigate to the application directory or create it if it doesn't exist
if [ ! -d "/home/ubuntu/deploy" ]; then
    mkdir -p /home/ubuntu/deploy
fi

cd /home/ubuntu/deploy

# Proceed with your existing deployment steps
