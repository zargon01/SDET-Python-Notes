from abc import ABC, abstractmethod


class College(ABC):
    @abstractmethod
    def attendance():
        pass

class Department(College):
    def __init__(self, hod, faculty, student, faculty_pre, student_pre):
        self.hod = hod
        self.faculty = faculty
        self.student = student
        self.faculty_pre = faculty_pre
        self.student_pre = student_pre

    def attendance(self):
        absent_students = self.student - self.student_pre
        absent_faculty = self.faculty - self.faculty_pre

        print(f"{absent_faculty} faculties are absent")
        print(f"{absent_students} students are absent")


def main():
    hod_name = input()
    department = input()
    no_of_faculty = int(input())
    no_of_student = int(input())
    no_of_faculty_pre = int(input())
    no_of_student_pre = int(input())

    obj = Department(hod_name,no_of_faculty,no_of_student,no_of_faculty_pre,no_of_student_pre)

    print(f"Department: {department}")
    print(f"Department Hod: {hod_name}")
    obj.attendance()


if __name__ == "__main__":
    main()