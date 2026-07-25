import StudentManager
class Teacher:

    def __init__(self, password , name ):
        self.password = password
        self.name = name
    
    def edit_grade(self, manager, student_id, course, grade):

     student = manager.find_student(student_id)

     if student is None:
        raise ValueError("Student not found")

     if not 0 <= grade <= 20:
        raise ValueError("Grade must be between 0 and 20")

     if course not in student.grades:
        raise ValueError("Course not found")

     student.grades[course] = grade
     
     
    def add_grade(self, manager, student_id, course, grade):

     student = manager.find_student(student_id)

     if student is None:
        raise ValueError("Student not found")
    
     if course in student.grades:
       raise ValueError("This course already has a grade")

     if not 0 <= grade <= 20:
        raise ValueError("Grade must be between 0 and 20")

     student.grades[course] = grade
            