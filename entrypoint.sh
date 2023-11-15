pip3 install -r requirements.txt --verbose
gunicorn -w 4 --chdir ./src 'service:app'