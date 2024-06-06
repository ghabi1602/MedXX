from flask_sqlalchemy import SQLAlchemy
#initialising SQLAlchemy
db = SQLAlchemy()

#At initialision, thses parameters are set
def init_db():
    from .models.user import User
    from .models.doctor import Doctor
    from .models.patient import Patient
    from .models.message import Message
    #creates all instance and save to database
    db.create_all()