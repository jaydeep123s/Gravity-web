#!/bin/bash

# Print a message indicating the start of the deployment
echo "Starting deployment..."

# Navigate to the application directory
cd /home/ubuntu/Gravity-web

# Activate the virtual environment (if used)
source venv/bin/activate

# Install any dependencies (if needed)
pip install -r requirements.txt

# Run the Flask application (make sure it listens on all interfaces)
export FLASK_APP=app.py
export FLASK_ENV=production

# Kill any existing Flask process running on port 80 (optional, depends on your setup)
sudo fuser -k 5000/tcp

# Start the Flask app on port 5000
nohup flask run --host=0.0.0.0 --port=5000 &

# Print a message indicating the deployment has completed
echo "Deployment completed."
