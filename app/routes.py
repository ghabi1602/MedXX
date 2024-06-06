from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Doctor, User, Patient
from .models import Patient
from .db_storage import db

#initialising a blue print
bp = Blueprint('routes', __name__)

#function that returns the landing page
@bp.route('/', strict_slashes=False)
def home():
    """route to the landing page"""
    return render_template('index2.html')


#function that returns the lsit of active users to respective dashboard
@bp.route('/dashboard')
@login_required
def dashboard():
    """route to list of active users to respective dashboard"""
    doctors = Doctor.query.all()
    patients = Patient.query.all()
    return render_template('dashboard.html',user=current_user,
                           doctors=doctors,
                           patients=patients)


#function that render the doctor's dashboard
@bp.route('/dashdoc')
@login_required
def dashdoc():
    """route to doctor's dashboard"""
    return render_template('dashdoc.html')


#function that renders the patient's dashboard
@bp.route('/dashpat')
@login_required
def dashpat():
    """function that returns the patient's dashboard"""
    return render_template('dashpat.html')