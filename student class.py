class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def calculate_grade(self):
        if self.marks >= 90:
            grade = 'A'
        elif self.marks >= 80:
            grade = 'B'
        elif self.marks >= 70:
            grade = 'C'
        else:
            grade = 'F'

        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", grade)

# Get input
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

# Create object
s = Student(name, marks)
s.calculate_grade()
