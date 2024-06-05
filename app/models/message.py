from ..db_storage import db
from .base_model import BaseModel

time = "%Y-%m-%d %H:%M:%S.%f"

class Message(BaseModel):
    __tablename__ = "messages"
    #id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.String(60), db.ForeignKey('users.id', name="fk_message_user_id"), nullable=False)
    receiver_id = db.Column(db.String(60), db.ForeignKey('users.id', name="fk_message_reciver_id"), nullable=False)
    message = db.Column(db.Text, nullable=False)
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