from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/nushhack'


db = SQLAlchemy(model_class=declarative_base())
db.init_app(app)


from app import routes
