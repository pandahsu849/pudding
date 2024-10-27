from flask import Blueprint, request, redirect, url_for
import mysql.connector

create_bp = Blueprint('create_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'jason921221849',
    'host': 'localhost',
    'database': 'employeesystem'  # Database name
}

# Route to add a new department
@create_bp.route('/add_department', methods=['POST'])
def add_department():
    department_name = request.form['department_name']
    project_id = request.form['project_id']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Insert data into the departments table
    insert_department_query = "INSERT INTO departments (department_name, project_id) VALUES (%s, %s)"
    cursor.execute(insert_department_query, (department_name, project_id))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return redirect(url_for('read_bp.index'))

# Route to add a new employee
@create_bp.route('/add_employee', methods=['POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    department_id = request.form['department_id']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Insert data into the employees table
    insert_employee_query = "INSERT INTO employees (first_name, last_name, department_id) VALUES (%s, %s, %s)"
    cursor.execute(insert_employee_query, (first_name, last_name, department_id))
    conn.commit()

    return redirect(url_for('read_bp.index'))
    
# Route to add a new project
@create_bp.route('/add_project', methods=['POST'])
def add_project():
    project_name = request.form['project_name']
    project_description = request.form['project_description']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    insert_query = "INSERT INTO projects (project_name, project_description) VALUES (%s, %s)"
    cursor.execute(insert_query, (project_name, project_description))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('read_bp.index'))
