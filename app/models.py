from . import db

class Task(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100), nullable = False)
  status = db.Column(db.String(20), default = "pending")
  username = db.Column(db.String(20), db.ForeignKey('user_credentials.username'), nullable=False)

class User_Credentials(db.Model):
    __tablename__ = 'user_credentials'
    username = db.Column(db.String(20), primary_key=True, nullable = False)
    password = db.Column(db.String(10), nullable = False)