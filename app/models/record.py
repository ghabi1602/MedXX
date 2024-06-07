from ..db_storage import db
from .base_model import BaseModel

time = "%Y-%m-%d %H:%M:%S.%f"

class Record(BaseModel):
    __tablename__ = "records"
    
    doctor_id = db.Column(db.String(60), db.ForeignKey('users.id', name="fk_record_doctor_id"), primary_key=True)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id', name="fk_record_user_id"), primary_key=True)
    allergies = db.Column(db.String(1000), nullable=True)
    diagnosis = db.Column(db.String(6000), nullable=False)
    medication = db.Column(db.String(500), nullable=True)
    medical_history = db.Column(db.String(1000), nullable=True)
    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict