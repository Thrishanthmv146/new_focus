print(f"Student Marks Analyzer\n")
class students_marks_Analyzer:
    def __init__(self):
        self.students={
                "Rahul": 75,
                "Priya": 32,
                "Arun": 88,
                "Sneha": 25,
                "Kiran": 60}
        self.passed_students={}
        self.failed_students={}
        self.stu_marks=[]
        self.high_mark=[]
    def students_marks(self):
        for student,marks in self.students.items():
            print(f"{student}--{marks}")
    def pass_students(self):
        print("\nStudents who passed")
        count=0
        for student,marks in self.students.items():
            if marks>=35:
                stu=student
                self.passed_students[stu]=marks
                count+=1
        print(f"{self.passed_students}")
        print(f"\nNumber of students passed: {count}")
    def fail_students(self):
        print("\nStudents who failed")
        for student,marks in self.students.items():
            if marks<35:
                stu=student
                self.failed_students[stu]=marks
        print(f"{self.failed_students}")
    def highest_marks(self):
        high_mark=0
        print("\nStudent with highest marks")
        for student,marks in self.students.items():
            self.stu_marks.append(marks)
            for item in self.stu_marks:
                if item>high_mark:
                    stu=student
                    high_mark=item
                    self.high_mark.append(high_mark)
        print(f"{stu}--{high_mark}")
    def average_marks(self):
        total_students=len(self.students)
        total_marks=0
        for marks in self.students.values():
            total_marks+=marks
            average_marks=total_marks/total_students
        print(f"\nAverage Marks---{average_marks}")
school= students_marks_Analyzer()
school.students_marks()
school.pass_students()
school.fail_students()
school.highest_marks()
school.average_marks()


