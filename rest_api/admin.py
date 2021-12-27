from sqlite3 import adapt
import flask
from flask_admin.contrib.mongoengine import ModelView
# from flask_admin.contrib.mongoengine.filters import FilterEqual, FilterLike
from rest_api.models import User
from app import admin

class UserModelView(ModelView):
    res = 'asd'




admin.add_view(ModelView(User))