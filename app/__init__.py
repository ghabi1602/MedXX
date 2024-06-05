from .db_storage import db
from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_migrate import Migrate
from .models import User, Doctor, Patient, Message

login_manager = LoginManager()
socketio = SocketIO()
migrate = Migrate()


def create_app():
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://medx_dev:betty@localhost/medx_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    socketio.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    

    with app.app_context():
        from . import routes, auth, chat
        app.register_blueprint(routes.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(chat.bp)
    
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    return app