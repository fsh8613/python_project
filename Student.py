import matplotlib.pyplot as plt
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
     if len(self.grades) == 0:
        return 0
     gpa = sum(self.grades.values()) / len(self.grades)
     return gpa
  
    def get_level(self):
       if  20 >= self.calculate_gpa >=18 :
          return "Excellent"
       elif 18 > self.calculate_gpa >=13 : 
          return "Average"
       elif 13 > self.calculate_gpa >=0 : 
          return "Weak"
   
    def edit_grade(self, course, grade):

     if not 0 <= grade <= 20:
        raise ValueError("Grade must be between 0 and 20")

     if course not in self.grades:
        raise ValueError("Course not found")

     self.grades[course] = grade
    
    def show_grades_chart(self):

     courses = list(self.grades.keys())
     grades = list(self.grades.values())

     plt.bar(courses, grades)

     plt.title(self.name + "'s Grades")
     plt.xlabel("Courses")
     plt.ylabel("Grade")

     plt.ylim(0, 20)

     plt.show()