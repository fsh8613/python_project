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
    
    def find_student(self, student_id):
     for student in self.students:
        if student.student_id == student_id:
            return student

     return None
    def remove_student(self, student_id):
      student = self.find_student(student_id)

      if student:
        self.students.remove(student)
        print(f"Student {student.name} removed successfully")
      else:
        raise ValueError("Student not found")
    
    def failed_students(self):
     failed = []

     for student in self.students:
        if student.calculate_gpa() < 13:
            failed.append(student)

     return failed
 
    def best_students(self):
        

     sorted_students = sorted(
        self.students,
        key=lambda student: student.calculate_gpa(),
        reverse=True
    )

     result = []

     if len(sorted_students) == 0:
        return result

     rank = 1
     last_gpa = sorted_students[0].calculate_gpa()

     for student in sorted_students:

        if student.calculate_gpa() != last_gpa:
            rank += 1
            last_gpa = student.calculate_gpa()

        if rank > 3:
            break

        result.append(
            f"{rank}. {student.name} - GPA: {student.calculate_gpa():.2f}"
        )

     return result