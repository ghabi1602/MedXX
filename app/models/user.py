from ..db_storage import db
from .base_model import BaseModel
from flask_login import UserMixin

class User(UserMixin, BaseModel):
    __tablename__ = "users"
    fullname = db.Column(db.String(300))
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(26), nullable=False)
    is_doctor = db.Column(db.Boolean, default=False)
    is_online = db.Column(db.Boolean, default=False)
    blood_group = db.Column(db.String(60), nullable=True)
    genotype = db.Column(db.String(60), nullable=True)
    location = db.Column(db.String(60), nullable=True)
    dob = db.Column(db.DateTime, nullable=False)
    allergies = db.Column(db.String(250), nullable=True)
    weight = db.Column(db.Integer, nullable=True) 