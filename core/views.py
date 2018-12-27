from flask import current_app, Blueprint, render_template, redirect, url_for, request, session

main_app = Blueprint('main_app', __name__, template_folder='templates')

@main_app.route('/')
def home():
    return render_template('home.html')