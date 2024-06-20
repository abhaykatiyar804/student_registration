import abc
from abc import ABC

from student_registration.student import Student


class IStudentStore(ABC):

    @abc.abstractmethod
    def register_student(self, student: Student):
        pass

    @abc.abstractmethod
    def unregister_student(self, student_id: str):
        pass

    @abc.abstractmethod
    def list_student(self, student_id: str) -> Student:
        pass

    @abc.abstractmethod
    def list_all_student(self) -> list[Student]:
        pass
