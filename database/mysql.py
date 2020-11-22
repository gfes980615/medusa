from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from server.server import app

# MySql datebase
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@127.0.0.1:3306/diana"

db = SQLAlchemy(app)
