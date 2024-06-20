from student_registration.istudent_repo import IStudentStore
from student_registration.student import Student


class StudentRegistrationService:
    def __init__(self, store: IStudentStore):
        self.store = store

    def register_user(self, name: str, student_id: str) -> Student:
        student = Student(name, student_id)
        self.store.register_student(student)
        return student

    def remove_student(self, student_id: str):
        self.store.unregister_student(student_id)

    def list_student(self, student_id: str) -> Student:
        student: Student = self.store.list_student(student_id)
        return student

    def list_all_student(self) -> list[Student]:
        return self.store.list_all_student()
