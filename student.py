class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        # Corrected string formatting
        return f"I am {self.name} who majors in {self.major}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    major = input("Major: ")
    return Student(name, major)

if __name__ == "__main__":
    main()

