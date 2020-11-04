#! /bin/bash
source venv/bin/activate
env FLASK_APP=app.py FLASK_DEBUG=1 flask run
deactivate
