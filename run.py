from flask import Flask, g
from core.views import main_app
from flask_jsglue import JSGlue

# intialise, register blueprints and set configs
app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(main_app)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# set custom static folder
app.static_url_path = app.config.get('STATIC_FOLDER')
app.static_folder = app.root_path + app.static_url_path

# library bindings
JSGlue(app)