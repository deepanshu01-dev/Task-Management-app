# 📝 Task Management App (Flask)

A simple task management app built with Flask. Users can register, log in, and manage their personal tasks. Each user has a private task list with options to create, update, and delete tasks. Task status cycles between `Pending`, `Working`, and `Done`.

## 🚀 Features

- ✅ User registration and login
- 🔐 Session-based authentication
- 🧍 Personalized task pages (each user sees only their own tasks)
- ➕ Add tasks
- 🔄 Toggle task status (Pending → Working → Done → Pending)
- 🗑️ Delete individual tasks
- 🔥 Clear all tasks
- 🚪 Logout functionality
- ❌ Delete your own account
- 💾 SQLAlchemy integration with a SQLite database

## ⚙️ Tech Stack

- **Python 3.x**
- **Flask**
- **Flask SQLAlchemy**
- **Flask-Login** (optional, if you're using it)
- **Jinja2** for templates
- **HTML/CSS (basic UI)**

---

> 💡 _Each user gets their own task list — tasks are private and secure._  
> 🔒 _Logged-out users can't access any task data._

