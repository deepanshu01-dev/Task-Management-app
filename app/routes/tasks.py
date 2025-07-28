from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app import db
from app.models import Task


tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/view_tasks')
def view_tasks():
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  
  tasks = Task.query.all()
  return render_template('tasks.html', tasks=tasks)


@tasks_bp.route('/add', methods=['POST'])
def add_task():
  if 'user' not in session:
    return redirect(url_for('auth.login'))
  
  title = request.form.get('title')
  if title:
    new_task = Task(title=title, status = 'pending')
    db.session.add(new_task)
    db.session.commit()
    flash("Task Added Successfully", "success")

  return redirect(url_for('tasks.view_tasks'))
  

@tasks_bp.route('/toggle/<int:id>', methods=['POST'])
def toggle_status(id):
  task = Task.query.get(id)
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
  task = Task.query.get(id)
  if task:
    db.session.delete(task)
    db.session.commit()
    flash("all task cleared", 'info')
  return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear')
def clear():
  Task.query.delete()
  db.session.commit()
  flash("all task cleared!",  'info')
  return redirect(url_for('tasks.view_tasks'))

