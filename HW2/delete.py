from flask import Blueprint, request, redirect, url_for
import mysql.connector

delete_bp = Blueprint('delete_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'jason921221849',
    'host': 'localhost',
    'database': 'employeesystem'  # Database name
}

# Route to delete selected departments
@delete_bp.route('/delete_departments', methods=['POST'])
def delete_departments():
    selected_ids = request.form.getlist('department_ids')  # Get selected department IDs
    
    if selected_ids:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Delete departments with specified IDs
        delete_query = "DELETE FROM departments WHERE department_id IN (%s)" % ','.join(['%s'] * len(selected_ids))
        cursor.execute(delete_query, tuple(selected_ids))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    return redirect(url_for('read_bp.index'))

# Route to delete selected employees
@delete_bp.route('/delete_employees', methods=['POST'])
def delete_employees():
    selected_employee_ids = request.form.getlist('employee_ids')  # Get selected employee IDs
    
    if selected_employee_ids:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Delete employees with specified IDs
        delete_employee_query = "DELETE FROM employees WHERE employee_id IN (%s)" % ','.join(['%s'] * len(selected_employee_ids))
        cursor.execute(delete_employee_query, tuple(selected_employee_ids))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    return redirect(url_for('read_bp.index'))

# Route to delete selected projects
@delete_bp.route('/delete_projects', methods=['POST'])
def delete_projects():
    selected_ids = request.form.getlist('project_ids')
    
    if selected_ids:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        delete_query = "DELETE FROM projects WHERE project_id IN (%s)" % ','.join(['%s'] * len(selected_ids))
        cursor.execute(delete_query, tuple(selected_ids))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    return redirect(url_for('read_bp.index'))

