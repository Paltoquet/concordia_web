from flask import Flask, url_for, render_template, request, jsonify
from datetime import datetime
from database import db

app = Flask(__name__)

# ------------------------- #
# ---------- API ---------- #

@app.route('/api/sensor', methods=['GET'])
def get_sensors():
    # Get all sensors values
    return jsonify(data=db.query(
        'SELECT * FROM sensors ORDER BY sensor_time DESC'
    ))

@app.route('/api/sensor/<sensor_name>', methods=['GET'])
def get_sensor(sensor_name):
    # Get all values for the specified sensor
    return jsonify(data=db.query(
        'SELECT * FROM sensors WHERE sensor_name = ? ORDER BY sensor_time DESC',
        [ sensor_name ]
    ))

@app.route('/api/sensor/<sensor_name>', methods=['PUT'])
def put_sensor(sensor_name):
    body = request.get_json()
    
    # Insert new value in database
    db.insert(
        'INSERT INTO sensors (sensor_name, sensor_value, sensor_time) VALUES (?, ?, ?)',
        [ sensor_name, body.get('value'), datetime.now() ]
    )

    return jsonify(status='OK')

# --------------------------- #
# ---------- INDEX ---------- #
        
@app.route('/', methods=['GET'])
def get_index():
    db.get()
    return render_template('index.html')

# -------------------------- #

@app.teardown_appcontext
def app_close(exception):
    db.close() # Disconnect database
