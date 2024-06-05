from ..db_storage import db
from .user import User

class Doctor(User):
    __tablename__ = "doctors"
    id = db.Column(db.String(60), db.ForeignKey('users.id', name="fk_doctor_user_id"), primary_key=True)
    specialty = db.Column(db.String(150), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }