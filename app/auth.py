from .db_storage import db
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import User
from .models import Doctor
from .models import Patient
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        log_user = User.query.filter_by(email=email).first()
        if log_user and check_password_hash(log_user.password, password):
            login_user(log_user)
            print("logged in successfully")
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Login failed. Check your email and password.')
            print("Login failed")
    return render_template('index2.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        is_doctor = request.form.get('is_doctor') == 'on'
        dob = request.form.get('dob')
        blood_group = request.form.get('blood_group')
        genotype = request.form.get('allergies')
        weight = request.form.get('weight')
        location = request.form.get('location')
        specialty = request.form.get('specialty')
        bio = request.form.get('bio')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        if User.query.filter_by(email=email).first():
            flash('Email address already registered', 'error')
            return redirect(url_for('auth.register'))

        new_user = Doctor(fullname=fullname,
                        username=username,
                        email=email,
                        password=hashed_password,
                        is_doctor=is_doctor,
                        dob=dob,
                        blood_group=blood_group,
                        genotype=genotype,
                        weight=weight,
                        location=location,
                        specialty=specialty,
                        bio=bio
                        ) if is_doctor else Patient(fullname=fullname,
                                                    username=username,
                                                    email=email,
                                                    password=hashed_password,
                                                    is_doctor=is_doctor,
                                                    dob=dob,
                                                    blood_group=blood_group,
                                                    genotype=genotype,
                                                    weight=weight,
                                                    location=location)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))