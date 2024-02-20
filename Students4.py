def mean_grade(grades: dict) -> float:
    if len(grades) == 0:
        return None
    
    grades = [x for x in grades.values()]
    grades = [item for row in grades for item in row]

    mean_grade = sum(grades) / len(grades)
    return mean_grade

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or self.finished_courses) and course in lecturer.courses and (1<=grade<=10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self) -> str:
        res = f"Имя: {self.name}"
        res += f"\nФамилия: {self.surname}"

        mg = mean_grade(self.grades)
        if mg is not None:
            res += f"\nСредняя оценка за домашние задания: {mg:.2f}"
        else:
            res += f"\nОценок за домашние задания пока нет."

        res += f"\nКурсы в процессе изучения: {' '.join(self.courses_in_progress)}"
        res += f"\nЗавершенные курсы: {' '.join(self.finished_courses)}"
        return res
    
    def get_mean_grade(self) -> float:
        return mean_grade(self.grades) or 0.0
    
    def get_mean_grade_by_course(self, course: str) -> float:
        if course not in self.grades:
            return None
        
        return sum(self.grades[course]) / len(self.grades[course])
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Student):
            raise ValueError("Compare error")
        
        return self.get_mean_grade() == __value.get_mean_grade()
    
    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Student):
            raise ValueError("Compare error")
        
        return self.get_mean_grade() > __value.get_mean_grade()
    
    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Student):
            raise ValueError("Compare error")
        
        return self.get_mean_grade() < __value.get_mean_grade()

     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f"Имя: {self.name}"
        res += f"\nФамилия: {self.surname}"
        return res
    
    def attach_course(self, course: str):
        if course in self.courses_attached:
            raise ValueError(f"Course {course} already attached")
        else:
            self.courses_attached.append(course)
            
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.grades = {}

    def __str__(self):
        res = super().__str__()
        mg = mean_grade(self.grades)
        if mg is not None:
            res += f"\nСредняя оценка за лекции: {mg:.2f}"
        else:
            res += f"\nОценок за лекции пока нет"
        return res
    
    def get_mean_grade(self) -> float:
        return mean_grade(self.grades) or 0.0
    
    def get_mean_grade_by_course(self, course: str) -> float:
        if course not in self.grades:
            return None
        
        return sum(self.grades[course]) / len(self.grades[course])
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Lecturer):
            raise ValueError("Compare error")
        
        return self.get_mean_grade() == __value.get_mean_grade()
    
    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Lecturer):
            raise ValueError("Compare error")
        
        return self.get_mean_grade() > __value.get_mean_grade()
    
    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Lecturer):
            raise ValueError("Compare error")
        
        return self.get_mean_grade() < __value.get_mean_grade()
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise ValueError(f"Rate error")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student_2 = Student('Misha', 'Sipl', 'M')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ['Java']

best_lecturer = Lecturer('Vasya','Pupkin')
best_lecturer.courses += ['Python']
best_lecturer.courses += ['Java']

best_student.rate_lect(best_lecturer, 'Python', 10)
best_student_2.rate_lect(best_lecturer, 'Java', 9)
print (best_lecturer.grades)

reviewer = Reviewer("Anatoly", "Vasserman")
reviewer.attach_course("Python")
reviewer.rate_hw(best_student, "Python", 2)

print(best_lecturer)
print()
print(reviewer)
print()
print(best_student)
print()
print(best_student_2)
print("=" * 20)
reviewer.rate_hw(best_student_2, "Python", 3)
print(best_student_2 > best_student)
print(best_student_2 == best_student)

def mean_grade(objects: object, course: str) -> float:
    grades = [x.get_mean_grade_by_course(course) for x in objects]
    grades = [x for x in grades if x is not None]

    if not grades:
        raise ValueError(f"Grades for passed course {course} not found")
    
    return sum(grades) / len(grades)

def mean_student_grade(students: Student, course: str) -> float:
    return mean_grade(students, course)

def mean_lecturer_grade(lecturers: Lecturer, course: str) -> float:
    return mean_grade(lecturers, course)

print(f"{mean_student_grade([best_student, best_student_2], 'Python')  }")
print(f"{mean_lecturer_grade([best_lecturer], 'Java')  }")


