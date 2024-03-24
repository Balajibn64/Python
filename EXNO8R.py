class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\n")

# Creating instances of Student class
student1 = Student("Alice", 15, "9th")
student2 = Student("Bob", 14, "8th")

# Accessing attributes and method of Student class
student1.display_info()
student2.display_info()