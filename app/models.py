from . import db

class Task(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100), nullable = False)
  status = db.Column(db.String(20), default = "pending")

class User_Credentials(db.Model):
    username = db.Column(db.String(20), primary_key=True, nullable = False)
    password = db.Column(db.String(10), nullable = False)