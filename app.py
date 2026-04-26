from flask import Flask
from flask import render_template
from flask import send_from_directory,send_file

UPLOAD_FOLDER = '/root/Website/original'

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
    PATH="/root/Website/original/LucesComoFaros.png"
    return send_file(PATH, as_attachment=True)
