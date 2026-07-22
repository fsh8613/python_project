class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):

        for s in self.students:
            if s.student_id == student.student_id:
                raise ValueError("Student ID already exists!")

        self.students.append(student)