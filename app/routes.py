from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Doctor, User, Patient
from .models import Patient

bp = Blueprint('routes', __name__)

@bp.route('/', strict_slashes=False)
def home():
    return render_template('index2.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    doctors = Doctor.query.all()
    patients = Patient.query.all()
    return render_template('dashboard.html',user=current_user,
                           doctors=doctors,
                           patients=patients)