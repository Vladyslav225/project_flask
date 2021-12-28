from flask_admin.contrib.mongoengine import ModelView
from flask_admin.contrib.mongoengine.filters import FilterEqual, FilterLike
from models import User
from app import admin

class UserModelView(ModelView):
    print('UserModelView')
    column_filters = (
        FilterLike(User.name, 'name'),
        FilterEqual(User.last_name, 'last_name')
    )
print('admin')



admin.add_view(ModelView(User))