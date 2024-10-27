from flask import Blueprint, request, redirect, url_for
import mysql.connector

update_bp = Blueprint('update_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'jason921221849',
    'host': 'localhost',
    'database': 'employeesystem'  # Database name
}

# Route to update department information
@update_bp.route('/update_department/<int:department_id>', methods=['POST'])
def update_department(department_id):
    new_department_name = request.form.get(f'department_name_{department_id}')
    new_project_id = request.form.get(f'project_id_{department_id}')

    if not new_department_name:
        return "No content to update", 400
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    update_query = "UPDATE departments SET department_name = %s, project_id = %s WHERE department_id = %s"
    cursor.execute(update_query, (new_department_name, new_project_id, department_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('read_bp.index'))

# Route to update employee information
@update_bp.route('/update_employee/<int:employee_id>', methods=['POST'])
def update_employee(employee_id):
    new_first_name = request.form.get(f'first_name_{employee_id}')
    new_last_name = request.form.get(f'last_name_{employee_id}')
    new_department_id = request.form.get(f'department_id_{employee_id}')

    if not new_first_name or not new_last_name:
        return "No content to update", 400
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    update_employee_query = """
        UPDATE employees 
        SET first_name = %s, last_name = %s, department_id = %s 
        WHERE employee_id = %s
    """
    cursor.execute(update_employee_query, (new_first_name, new_last_name, new_department_id, employee_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('read_bp.index'))

# Route to update project information
@update_bp.route('/update_project/<int:project_id>', methods=['POST'])
def update_project(project_id):
    new_project_name = request.form.get(f'project_name_{project_id}')
    new_project_description = request.form.get(f'project_description_{project_id}')

    if not new_project_name:
        return "No content to update", 400

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    update_query = "UPDATE projects SET project_name = %s, project_description = %s WHERE project_id = %s"
    cursor.execute(update_query, (new_project_name, new_project_description, project_id))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('read_bp.index'))
