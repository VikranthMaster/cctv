from flask import Flask, render_template
import os
#In raspi do this from gpiozero import CPUTemperature()
#cpu = CPUTemperature()
#cpu.temperature

app = Flask(__name__)

lst = []
path = "test"
for x in os.listdir(path):
	lst.append(x)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/temperature")
def temperature():
    return render_template('temperature.html')

@app.route("/gate")
def stairs():
    return render_template('gate.html',list_dir = lst)

app.run(debug=True)
