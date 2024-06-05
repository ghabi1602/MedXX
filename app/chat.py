from .db_storage import db
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Message, Doctor, Patient
from . import socketio
from flask_socketio import send, emit, join_room, leave_room


bp = Blueprint('chat', __name__, url_prefix='/chat')

time = "%y/%b/%d %H:%M"

@bp.route('/')
@login_required
def chat():
    users = User.query.all()
    return render_template('chat.html', users=users)

@bp.route('/start_chat', methods=['GET', 'POST'])
@login_required
def start_chat():
    recipient_id = request.args.get('recipient_id')
    recipient = User.query.filter_by(id=recipient_id).first()
    if not recipient:
        flash('User not found.')
        return redirect(url_for('routes.dashboard'))
    
    patients = Patient.query.all()
    doctors = Doctor.query.all()
    messages= Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.receiver_id == recipient_id)) |
        ((Message.sender_id == recipient_id) & (Message.receiver_id == current_user.id))
    ).order_by(Message.created_at).all()
    return render_template('test_chatbox.html', 
                           user=current_user,
                           patients=patients,
                           doctors=doctors, 
                           recipient=recipient,
                           messages=messages)


@socketio.on('send_message')
@login_required
def handle_send_message(data):
    content = data["content"]
    recipient_id = data["recipient_id"]
    recipient = User.query.get(recipient_id)
    if not recipient:
        print("nothing")
        return

    new_message = Message(
        sender_id=current_user.id,
        receiver_id=data['recipient_id'],
        message = content
        )
    db.session.add(new_message)
    db.session.commit()
    
    emit('receive_message', {
        'content': new_message.message,
        'sender_id': new_message.sender_id,
        'sender': current_user.username,
        'recipient_id': new_message.receiver_id,
        'created_at': new_message.created_at.strftime(time)
        }, room=recipient_id + '_' + current_user.id)
    
    emit('receive_message', {
        'content': new_message.message,
        'sender_id': new_message.sender_id,
        'sender': current_user.username,
        'recipient_id': new_message.receiver_id,
        'created_at': new_message.created_at.strftime(time)
        }, room=current_user.id + '_' + recipient.id)
    
    

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('join_response', {'message': f'{current_user.username} has joined the room {room}.'}, room=room)


@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        current_user.is_online = True
        db.session.commit()
        emit('status_update', {'user_id': current_user.id, 'status': 'online'}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    if current_user.is_authenticated:
        current_user.is_online = False
        db.session.commit()
        emit('status_update', {'user_id': current_user.id, 'status': "offline"}, broadcast=True)


@bp.route('/get_messages/<recipient_id>', methods=['GET'])
@login_required
def get_messages(recipient_id):
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.recipient_id == recipient_id)) |
        ((Message.sender_id == recipient_id) & (Message.recipient_id == current_user.id))
    ).order_by(Message.created_at).all()

    return jsonify([
        {
            'content': message.message,
            'sender_id': message.sender_id,
            'sender': User.query.get(message.sender_id).username,
            'recipient_id': message.recipient_id,
            'created_at': message.created_at.strftime(time)
        } for message in messages
    ])