# Copyright 2021 Bugbound Ltd

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__)

app.config.from_object('settings')
app.url_map.strict_slashes = False

db = SQLAlchemy(app)

class Urlstore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(400))
    
db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Urlstore, methods=['POST', 'GET'])



@app.route('/')
def hello():
  return "urlstore\n"
  
@app.route("/clearall")
def clear_all_dbs():
  numrows = db.session.query(Urlstore).delete()
  
  db.session.commit()
  return "<h1 style='color:blue'>All Databases Have Been Wiped!</h1>"


