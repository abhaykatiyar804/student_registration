from student_registration.registration_service import StudentRegistrationService
from student_registration.student_store import StudentStore

registration_service = StudentRegistrationService(StudentStore())
registration_service.register_user("S1", "u1")
registration_service.register_user("S2", "u2")
registration_service.register_user("S3", "u3")
registration_service.register_user("S4", "u4")

print(registration_service.list_student("u2"))

registration_service.remove_student("u3")
print(registration_service.list_all_student())

print(registration_service.list_student("unknown_id"))
