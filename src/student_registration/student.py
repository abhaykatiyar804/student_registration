class Student:

    def __init__(self, name: str, student_id: str):
        self.name: str = name
        self.student_id: str = student_id

    def __repr__(self):
        return f"{self.student_id}:{self.name}"
