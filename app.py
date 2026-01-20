from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index_einar():
        return render_template('Einar.html')

@app.route("/Bere")
def index_bere():
        return render_template('Bere.html')
