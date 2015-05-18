# create 3 lists of students with grades
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    
    return total/len(numbers)
    
# get average of student    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    
    return 0.10 * homework + 0.30 * quizzes + 0.60 * tests
    
# get letter grade of student
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

# store students as integers    
students = [lloyd, alice, tyler]

# get class average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

# class average # and letter    
print get_class_average(students)
print get_letter_grade(get_class_average(students))
