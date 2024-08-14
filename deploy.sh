#!/bin/bash

echo "Starting deployment..."

# Navigate to the deployment directory
cd /home/ubuntu

# Ensure the script is executable
chmod +x deploy.sh

# Run deployment steps
./deploy.sh

echo "Deployment completed."
