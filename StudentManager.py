class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):

        for s in self.students:
            if s.student_id == student.student_id:
                raise ValueError("Student ID already exists!")

        self.students.append(student)
             
    def calculate_average_gpa(self):

        if len(self.students) == 0:
            return 0

        total = 0

        for student in self.students:
            total += student.calculate_gpa()

        return total / len(self.students)
    
    def get_best_student(self):
        return max(
        self.students,
        key=lambda student: student.calculate_gpa()
         )
        
    def get_course_average(self, course):

      total = 0
      count = 0

      for student in self.students:

        if course in student.grades:
            total += student.grades[course]
            count += 1

        if count == 0:
            print("this course is not exist!")
            return 0

        return total / count