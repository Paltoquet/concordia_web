@echo off

:: Configuration
set FLASK_APP=concordia.py

:: Run Flask
flask run --host=0.0.0.0 --port=2909
