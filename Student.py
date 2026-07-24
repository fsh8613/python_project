import matplotlib.pyplot as plt

class Student:


    def __init__(self, student_id, name):
       if student_id <= 0:
          raise ValueError("Student ID must be positive")
       self.student_id = student_id
       self.name = name
       self.grades = {}
   
        
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
    

     gpa = self.calculate_gpa()

     if gpa >= 18:
        return "Excellent"
     elif gpa >= 13:
        return "Average"
     else:
        return "Weak"
   
    def edit_grade(self, course, grade):

     if not 0 <= grade <= 20:
        raise ValueError("Grade must be between 0 and 20")

     if course not in self.grades:
        raise ValueError("Course not found")

     self.grades[course] = grade
    
    def show_grades_chart(self):
      if len(self.grades) == 0:
          print("No grades available!")
          return

      courses = list(self.grades.keys())
      grades = list(self.grades.values())

      plt.bar(courses, grades)

      plt.title(self.name + "'s Grades")
      plt.xlabel("Courses")
      plt.ylabel("Grade")

      plt.ylim(0, 20)

      plt.show() 
      
    def __str__(self):
     return f"ID: {self.student_id}, Name: {self.name}, GPA: {self.calculate_gpa():.2f}"