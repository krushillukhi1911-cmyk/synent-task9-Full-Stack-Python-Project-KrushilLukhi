# TaskMaster - Full Stack Task Management System

## Project Overview
TaskMaster is a complete, production-ready Full Stack Task Manager Web Application built with Flask and Python. It allows users to register, login, manage personal tasks, track progress, and view dashboard statistics.

## Features
- **User Authentication:** Registration, Login, Logout with secure session management.
- **Security:** Password Hashing, CSRF Protection.
- **Dashboard:** Personalized Dashboard with widgets for Total Tasks, Completed, Pending, and High Priority.
- **Task Management:** Create, Read, Update, and Delete (CRUD) Tasks.
- **Filtering & Searching:** Filter by Status and Priority, Sort by Date, Search by Title.
- **User Profile:** Manage Profile Information and update passwords.
- **Responsive UI:** Modern design with Bootstrap 5, custom CSS, and micro-animations.

## Installation Steps

1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Application URL
http://localhost:5000

## Technologies Used
- **Backend:** Python 3.11+, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Migrate
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
