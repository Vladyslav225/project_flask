from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine



app = Flask(__name__)
app.config.from_pyfile('./settings.py')
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = MongoEngine(app)

admin = Admin(
    app,
    name = 'TEST',
    template_mode='bootstrap3'
)

import core.views