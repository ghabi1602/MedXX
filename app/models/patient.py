from ..db_storage import db
from .user import User
from .doctor import Doctor

class Patient(User):
    __tablename__ = "patients"
    id = db.Column(db.String(60), db.ForeignKey('users.id', name="fk_patient_user_id"), primary_key=True)
    doctor_id = db.Column(db.String(60), db.ForeignKey('doctors.id', name="fk_doctor_patient_id"), nullable=True)
    medical_history = db.Column(db.Text, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }