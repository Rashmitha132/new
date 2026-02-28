from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_PIN = 18   # GPIO18 (Physical pin 12)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

led_state = False

@app.route('/')
def home():
    return render_template('index.html', state=led_state)

@app.route('/toggle')
def toggle():
    global led_state
    led_state = not led_state
    GPIO.output(LED_PIN, led_state)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)