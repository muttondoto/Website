from flask import Flask
from flask import render_template
from flask import send_from_directory,send_file

UPLOAD_FOLDER = '/root/Website/original/'

app = Flask(__name__)

@app.route("/")
def index_einar():
        return render_template('Einar.html')

@app.route("/<name>")
def html_template(name):
        html=name+".html"
        return render_template(html)
        
@app.route('/downloads/<name>')
def download_file(name):
    PATH=UPLOAD_FOLDER+name
    return send_file(PATH, as_attachment=True)
