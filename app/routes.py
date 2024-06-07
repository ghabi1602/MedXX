from flask import Blueprint, render_template, flash, request, redirect, url_for, make_response
from flask_login import login_required, current_user
from .models import Doctor, User, Patient, Record
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

#function that renders the record page
@bp.route('/records')
@login_required
def records():
    return render_template('record.html')

#function retrieves the record of a particular user
@bp.route('/records', methods=['POST'])
@login_required
def get_record():
    """get the record of a particular user using user_id"""
    email = request.form.get('search')
    user = Patient.query.filter_by(email=email).first()
    
    if not user:
        flash('user not found', 'error')
        return make_response(render_template('record.html'), 404)
    
    user_rec = Record.query.filter_by(user_id=user.id).all()

    doctors = Doctor.query.all()
    
    
    if not user_rec:
        flash('Patient dont have any record in our database yet!', 'error')
        return make_response(render_template('record.html'), 404)
    
    return render_template('record.html', user_rec=user_rec,
                           user=user,
                           doctors=doctors)


#displaying the new_record html
@bp.route('/records/new', methods=['GET'])
@login_required
def new_record():
    """renders page of the new record form"""
    return render_template('new_record.html')


#adding a new user record
@bp.route('/records/', methods=['POST'])
@login_required
def add_record():
    """add a user record"""
    user_rec = request.form.get('user_email')
    user = User.query.filter_by(email=user_rec).first()
    if not user:
        flash("user not found!!", 'error')
        return redirect(url_for('routes.new_record'))
    user_id = user.id
    doctor_id = current_user.id
    allergies = request.form.get('allergies')
    diagnosis = request.form.get('diagnosis')
    medical_history = request.form.get('medical_history')
    medication = request.form.get('medication')

    new_record = Record(user_id=user_id,
                        doctor_id=doctor_id,
                        allergies=allergies,
                        diagnosis=diagnosis,
                        medical_history=medical_history,
                        medication=medication)
    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for('routes.records'))

