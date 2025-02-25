#!/bin/bash

# Clone the repository (uncomment if needed)
# git clone <repository_url>

# Navigate to the project directory
cd "$(dirname "$0")"

# Install required packages
pip install -r requirements.txt

echo "Setup completed successfully."
