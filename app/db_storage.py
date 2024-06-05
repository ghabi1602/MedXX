from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def init_db():
    from .models.user import User
    from .models.doctor import Doctor
    from .models.patient import Patient
    from .models.message import Message
    db.create_all()