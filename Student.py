import StudentManager
class Student:

    manager = StudentManager()  

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}
        Student.manager.add_student(self)
        
    def add_grade(self, course, grade):
           if grade < 0 or grade > 20:
            raise ValueError("Grade must be between 0 and 20")
           self.grades[course] = grade
           
    def calculate_gpa(self):
        return sum(self.grades.values())/len(self.grades)
        