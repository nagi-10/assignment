student_grades = {}

def add_grade(student_name: str, grade: float):
    student_grades[student_name] = grade


def get_grade(student_name: str):
    return student_grades.get(student_name, "Student not found")

def display_grades():
    if student_grades:
        for student, grade in student_grades.items():
            print(f"{student}: {grade}")
    else:
        print("No grades available.")

add_grade("Alice", 90.5)
add_grade("Bob", 85.0)
add_grade("Charlie", 92.0)


print(get_grade("Alice"))  
print(get_grade("David"))  

display_grades()