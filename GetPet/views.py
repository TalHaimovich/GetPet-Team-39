from flask import Blueprint, request, send_from_directory
from flask.templating import render_template
import pathlib

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('css', path)