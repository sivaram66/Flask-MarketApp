from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# accept the key values from use // or flask can understand where database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] ='27e742971c14f594e67f6bba'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) #To store the password using hash(hash_passwords)
login_manager = LoginManager(app)
from market import routes # Import routes after creating the app instance