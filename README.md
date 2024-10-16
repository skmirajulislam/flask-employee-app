# Employee Management System

This is a simple Employee Management System built with Flask and SQLAlchemy, designed to manage employee records efficiently. The application supports basic CRUD (Create, Read, Update, Delete) operations for employee details.

## Functionality

### 1. **Insert Employee Records**
- Users can add new employee records by providing their name, designation, and salary through a form.
- The application validates the salary input to ensure it is not empty.

### 2. **View Employee Records**
- The application displays a list of all employee records in a structured format, including their name, designation, and salary.

### 3. **Update Employee Records**
- Users can update existing employee records by selecting an employee and modifying their details.
- The application allows changes to the name, designation, and salary fields.

### 4. **Delete Employee Records**
- Users can delete specific employee records from the database.
- The application confirms the deletion and provides feedback.

### 5. **Display Employee Details**
- The application has a dedicated route to display all employee details in a user-friendly format.
- If no employees are found, a message will be displayed indicating that there are no records.

## Technology Stack
- **Backend**: Flask
- **Database**: PostgreSQL with SQLAlchemy
- **HTML**: Jinja2 templates for rendering pages

## Installation
1. Clone the repository.
2. Set up a virtual environment.
3. Install the required packages using `pip install -r requirements.txt`.
4. Update the database URI in `app.py` with your own PostgreSQL database credentials.
5. Run the application with `python app.py`.

## Usage
- Start the application by running `python app.py` and access it via `http://localhost:8000` in your web browser.
- Follow the on-screen instructions to manage employee records.
