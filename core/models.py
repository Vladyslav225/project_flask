from datetime import datetime

from app import db

class User(db.Document):
    print('model User')
    name = db.StringField()
    last_name = db.StringField()
    created_date_time = db.DateTimeField(default=datetime.now)

#TODO class GET
#TODO class POST
#TODO class PUT
#TODO class TAG
#TODO class DELETE