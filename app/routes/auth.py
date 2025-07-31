from flask import Blueprint , render_template, redirect, url_for, session ,request, flash
from app.models import User_Credentials
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')    
    password = request.form.get('password')

    user = User_Credentials.query.filter_by(username=username, password = password).first()

    if user:
      session['user'] = username
      flash('login successfully', 'success')
      return redirect(url_for('tasks.view_tasks'))
  
    else:
        flash("invalid credentials!") 
        return redirect(url_for('auth.register'))
    
  return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
  if request.method == 'POST':
    username = request.form.get('username')    
    password = request.form.get('password')
    
    try:
      user_credentials = User_Credentials(username = username, 
      password = password)
      db.session.add(user_credentials)
      db.session.commit()
      flash("successfully registered!", 'success!')
      return redirect(url_for('auth.login'))

    except Exception as error:
      flash("You've Already Registered!", 'info')
      return redirect(url_for('auth.login'))

  return render_template('register.html')

@auth_bp.route('/logout')
def logout():
  session.pop('user', None)
  flash('logged out', 'info')
  return redirect(url_for('auth.login'))
