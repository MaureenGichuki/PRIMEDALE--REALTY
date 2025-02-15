from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)
mail = Mail()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    
    app.config.from_object(config_options[config_name])
    app.config['UPLOADED_PHOTO_DEST'] = "app/static/photos"

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    migrate = Migrate(app,db)

    
    # login_manager.init_app(app)
    mail.init_app(app)
   
    # configure UploadSet
    configure_uploads(app,photos)


   # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

   

    return app
