from flask import Blueprint, render_template
import mysql.connector

read_bp = Blueprint('read_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'jason921221849',
    'host': 'localhost',
    'database': 'employeesystem'
}

@read_bp.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Fetch departments, employees, projects
    cursor.execute("SELECT department_id, department_name, project_id FROM departments")
    departments = cursor.fetchall()

    cursor.execute("SELECT employee_id, first_name, last_name, department_id FROM employees")
    employees = cursor.fetchall()

    cursor.execute("SELECT project_id, project_name, project_description FROM projects")
    projects = cursor.fetchall()

    # SQL JOIN query
    join_query = """
    SELECT 
        departments.department_id,
        departments.department_name,
        projects.project_name,
        projects.project_description,
        employees.employee_id,
        employees.first_name,
        employees.last_name
    FROM 
        departments
    LEFT JOIN 
        projects ON departments.project_id = projects.project_id
    LEFT JOIN 
        employees ON departments.department_id = employees.department_id
    """
    cursor.execute(join_query)
    joined_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', departments=departments, employees=employees, projects=projects, joined_data=joined_data)
