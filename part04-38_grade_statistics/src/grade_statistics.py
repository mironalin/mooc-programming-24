# Write your solution here
def input_data():
    exam = []
    exercises = []
    while True:
        str = input("Exam points and exercises completed: ")
        if str == "":
            break
        str = str.split(" ")

        exam.append(int(str[0]))
        exercises.append(int(str[1]))
    
    return exam, exercises

def points_average(exam, exercises):
    sum_exam = sum(i for i in exam)
    sum_points = sum(i // 10 for i in exercises)
    
    return (sum_exam + sum_points) / len(exam) 

def pass_percentage(exam, exercises):
    passed = 0
    for i in range(len(exam)):
        if exam[i] >= 10 and exam[i] + exercises[i] // 10 >= 15:
            passed += 1
    return passed / len(exam) * 100      
    
def calculate_grades(exam, exercises):
    grades = []
    for i in range(len(exam)):
        total = exam[i] + exercises[i] // 10
        if exam[i] >= 10 and exam[i] + exercises[i] // 10 >= 15:
            if 28 <= total <= 30:
                grades.append(5)
            elif 24 <= total <= 27:
                grades.append(4)
            elif 21 <= total <= 23:
                grades.append(3)
            elif 18 <= total <= 20:
                grades.append(2)
            elif 15 <= total <= 20:
                grades.append(1)
        else:
            grades.append(0)
    return grades
    
def print_grades(grades):
    for i in range(5, -1, -1):
        no = 0
        for grade in grades:
            if grade == i:
                no += 1
        print(f"  {i}: {"*" * no}")
    
def print_stats(exam, exercises):
    print("Statistics:")
    print(f"Points average: {points_average(exam, exercises):.1f}")
    print(f"Pass percentage: {pass_percentage(exam,exercises):.1f}")
    print("Grade distribution:")
    print_grades(calculate_grades(exam, exercises))

def start():
    exam, exercises = input_data()
    print_stats(exam, exercises)
    
start()
