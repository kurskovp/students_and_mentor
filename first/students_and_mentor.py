class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname, teaching_course):
        self.name = name
        self.surname = surname
        self.teaching_course = teaching_course



class Lecturer(Mentor):
    def __init__(self,name, surname, teaching_course):
        Mentor. __init__ (self,name, surname, teaching_course)


class Reviewer(Mentor):
    def __init__(self,name, surname, teaching_course):
        Mentor. __init__ (self,name, surname, teaching_course)

    def set_student_grade(self, student, cours, grade):
        if cours in student.courses_in_progress:
            if cours in self.teaching_course:
                student.grades[cours] = grade
            else:
                print(f'Преподаватель этот курс не должен проверять - {cours}')
        else:
            print(f'Студент не записан на данный курс - {cours}')



# Проверочный блок:

john = Student("John", "Smith", "male")
john.courses_in_progress = ["Python", "Git"]
print(john.name)
print(john.courses_in_progress[1])

rev_1 = Reviewer('Nic', 'Popov', ["Math", "Physics", "Python"])
rev_1.set_student_grade(john, 'Math', 4)
rev_1.set_student_grade(john, 'Python', 5)
print(john.grades)
