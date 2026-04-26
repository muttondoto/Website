from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def index_einar():
        return render_template('Einar.html')

@app.route("/Bere")
def index_bere():
        return render_template('Bere.html')
        
@app.route("/Postulado")
def index_postulado():
        return render_template('Postulado.html')

@app.route('/downloads/<name>')
def download_file(name):
        return send_from_directory(app.config["./original"], name)
