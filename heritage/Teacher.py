from Human import Human

class Teacher(Human):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self._teacher_id = teacher_id

    def presentation(self):
        super().presentation()
        print(f"My teacher ID is {self._teacher_id}.")
        