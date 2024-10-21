class Student:
    ...


def main():
    student = get_student_info()
    print(f"{student.name} from {student.house}")

def get_student_info():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student # this method is just by returning using a tuple but by another way




if __name__ == "__main__":
    main()