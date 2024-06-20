from student_registration.exceptions import StudentAlreadyExist, StudentNotExist
from student_registration.istudent_repo import IStudentStore
from student_registration.student import Student


class StudentStore(IStudentStore):

    def __init__(self):
        self.storage_path = "./storage"

    def register_student(self, student: Student):

        students = self.__get_students()
        for _student in students:
            if _student.split(":")[0] == student.student_id:
                raise StudentAlreadyExist()

        with open(self.storage_path, "a") as file:

            file.write(str(student) + "\n")

    def unregister_student(self, student_id: str):
        students_write = []
        students: list[str] = self.__get_students()

        for student in students:
            if student.split(":")[0] != student_id:
                students_write.append(student)

        with open(self.storage_path, "w") as file:
            file.writelines(students_write)

    def __get_students(self):
        with open(self.storage_path, "r") as file:
            students = file.readlines()
        return students

    def list_student(self, student_id: str) -> Student:

        students = self.__get_students()
        for student in students:
            if student.split(":")[0] == student_id:
                sid, name = student.split(":")
                return Student(name, sid)
        raise StudentNotExist()

    def list_all_student(self) -> list[Student]:
        result = []
        students: list[str] = self.__get_students()
        for student in students:
            sid, name = student.split(":")
            result.append(Student(name, sid))
        return result
