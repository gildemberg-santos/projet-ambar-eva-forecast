#! /bin/bash
source venv/bin/activate
env FLASK_APP=app.py flask run
deactivate
