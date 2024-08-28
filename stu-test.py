from student import Student

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    major = input("Major: ")
    return Student(name, major)

if __name__ == "__main__":
    main()
