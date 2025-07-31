from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app import db
from app.models import Task
from app.models import User_Credentials


tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/view_tasks')
def view_tasks():
  username = session.get('user')
  if  not username:
    return redirect(url_for('auth.login'))
  
  user_tasks = Task.query.filter_by(username=username).all()
  return render_template('tasks.html', tasks=user_tasks)


@tasks_bp.route('/add', methods=['POST'])
def add_task():
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  
  title = request.form.get('title')
  username = session['user']
  if title:
    new_task = Task(title=title, status = 'pending', username=username)
    db.session.add(new_task)
    db.session.commit()
    flash("Task Added Successfully", "success")

  return redirect(url_for('tasks.view_tasks'))
  

@tasks_bp.route('/toggle/<int:id>', methods=['POST'])
def toggle_status(id):
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  username = session.get('user')
  task = Task.query.filter_by(id=id, username=username).first()
  if task:
    if task.status == "pending":
      task.status = "working"

    elif task.status == "working":
      task.status = "Done"

    else:
      task.status = "pending"

    db.session.commit()
  return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  
  username = session['user']
  task = Task.query.filter_by(id=id, username=username).first()
  if task:
    db.session.delete(task)
    db.session.commit()
    flash("task Deleted", 'info')
  return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear')
def clear():
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  username = session['user']
  Task.query.filter_by(username=username).delete()
  db.session.commit()
  flash("all task cleared!",  'info')
  return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete_account', methods=['POST'])
def delete_account():
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  
  username = session.get('user')
  user = User_Credentials.query.filter_by(username=username).first()
  if user:
    Task.query.filter_by(username=username).delete()
    db.session.delete(user)
    db.session.commit()
    session.clear()
    flash('Your Account and all the data have been deleted!', 'info')
    return redirect(url_for('auth.login'))
  
  flash('User not found.', 'error')
  return redirect(url_for('auth.register'))

