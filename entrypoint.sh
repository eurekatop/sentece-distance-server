#!/bin/sh

# Check if installed.txt exists
if [ ! -f "installed.txt" ]; then
    # Run pip3 install
    pip3 install -r requirements.txt --verbose

    # Create installed.txt after successful installation
    touch installed.txt
fi

# start server
gunicorn -w 1 --chdir ./src -b 0.0.0.0:8000 'service:app'
