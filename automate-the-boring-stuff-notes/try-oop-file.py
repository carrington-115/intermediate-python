class Student:
    def __init__(self, first_name, last_name, home_address):
        if not first_name or not last_name:
            raise ValueError("Invalid name")
        self.first_name = first_name
        self.last_name = last_name
        self.home_address = home_address

    def __str__(self):
        return f"This is {self.first_name} from {self.home_address}"

def main():
    student = get_student_info()
    print(student)
    print(f"{student.first_name} {student.last_name} from {student.home_address}")

def get_student_info():
    first_name = input("Frist name: ")
    last_name = input("Last name: ")
    home_address = input("address: ")
    return Student(first_name, last_name, home_address) # this method is just by returning using a tuple but by another way

if __name__ == "__main__":
    main()