class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    name = ''
    surname =''
    teaching_course =[]

    def __init__(self, name, surname,):
        self.name = name
        self.surname = surname
        self.teaching_course = []



class Lecturer(Mentor):
    def __init__(self,name, surname, teaching_course):
        Mentor. __init__ (self,name, surname, teaching_course)

class Reviewer(Mentor):
    def __init__(self,name, surname, teaching_course):
        Mentor. __init__ (self,name, surname, teaching_course)


