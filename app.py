from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from model import Student, StudentManager

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'studentdb'

# Initialize MySQL
mysql = MySQL(app)
student_manager = StudentManager(mysql)

@app.route('/')
def index():
    students = student_manager.get_all_students()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        studentname = request.form['studentname']
        department = request.form['department']
        phone = request.form['phone']

        new_student = Student(studentname, department, phone)
        student_manager.add_student(new_student)

        flash('Student added successfully!')
        return redirect(url_for('index'))
    
    return render_template('add_student.html')

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        studentname = request.form['studentname']
        department = request.form['department']
        phone = request.form['phone']

        updated_student = Student(studentname, department, phone)
        student_manager.update_student(id, updated_student)

        flash('Student updated successfully!')
        return redirect(url_for('index'))

    student = student_manager.get_student(id)
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    student_manager.delete_student(id)
    flash('Student deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
