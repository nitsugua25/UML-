from Teacher import Teacher
from Student import Student
from Human import Human

if __name__ == "__main__":
    
    # create objects
    human = Human("Alice", 20)
    teacher = Teacher("John", 30, "T001")
    student = Student("Alice", 20, "S001")
    
    
    # use of the object's presentation method
    human.presentation()
    print("--------------------")
    teacher.presentation()
    print("--------------------")
    student.presentation()
    print("--------------------")