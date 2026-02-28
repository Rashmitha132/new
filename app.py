from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO Pins
LED1 = 18   # GPIO18
LED2 = 23   # GPIO23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

led1_state = False
led2_state = False

@app.route('/')
def home():
    return render_template('index.html', 
                           led1=led1_state, 
                           led2=led2_state)

@app.route('/toggle1')
def toggle1():
    global led1_state
    led1_state = not led1_state
    GPIO.output(LED1, led1_state)
    return redirect(url_for('home'))

@app.route('/toggle2')
def toggle2():
    global led2_state
    led2_state = not led2_state
    GPIO.output(LED2, led2_state)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)