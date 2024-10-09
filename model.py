from flask_mysqldb import MySQL
import MySQLdb.cursors

class Student:
    def __init__(self, studentname, department, phone):
        self.studentname = studentname
        self.department = department
        self.phone = phone


class StudentManager:
    def __init__(self, mysql):
        self.mysql = mysql

    def add_student(self, student):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('INSERT INTO student (studentname, department, phone) VALUES (%s, %s, %s)', 
                           (student.studentname, student.department, student.phone))
            self.mysql.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def get_all_students(self):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM student')
        students = cursor.fetchall()
        cursor.close()
        return students

    def get_student(self, student_id):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM student WHERE studentid=%s', (student_id,))
        student = cursor.fetchone()
        cursor.close()
        return student

    def update_student(self, student_id, student):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('UPDATE student SET studentname=%s, department=%s, phone=%s WHERE studentid=%s', 
                           (student.studentname, student.department, student.phone, student_id))
            self.mysql.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def delete_student(self, student_id):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('DELETE FROM student WHERE studentid=%s', (student_id,))
            self.mysql.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
