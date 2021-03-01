from flask import Flask, render_template, request
from randomnumberfactapi import request_random_number_face
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        json_data = request_random_number_face(number)

        return render_template('index.html', json_data=json_data)
    else:
        return render_template('index.html')
