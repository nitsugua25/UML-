from Human import Human

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def presentation(self):
        super().presentation()
        print(f"My student ID is {self._student_id}.")
        