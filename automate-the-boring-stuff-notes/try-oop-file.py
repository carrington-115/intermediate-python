class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return "This is a student"

def main():
    student = get_student_info()
    # print(f"{student.name} from {student.house}")
    print(student)

def get_student_info():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # this method is just by returning using a tuple but by another way
   
if __name__ == "__main__":
    main()