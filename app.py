from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine

import os
get_secret_key = os.urandom(16)


app = Flask(__name__)

app.secret_key = get_secret_key

app.config.from_pyfile('./settings.py')
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = MongoEngine(app)

admin = Admin(
    app,
    name = 'Wine Store',
    template_mode='bootstrap3'
)
print('app')
import core.views
import core.admin
