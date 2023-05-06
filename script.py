#!/usr/bin/python3

import Adafruit_DHT
Sensor = Adafruit_DHT.DHT22
SensorPin = 17

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update')
def update():

    humidity, temperature = Adafruit_DHT.read_retry(Sensor, SensorPin)

    if humidity is not None and temperature is not None:
        return jsonify({'temperature': temperature, 'humidity': humidity})

    else:
        return jsonify({'temperature': 'Error', 'humidity': 'Error'})

if __name__ == '__main__':

    app.run(debug = True, host = '0.0.0.0')