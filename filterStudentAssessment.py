def assessmentStudent(student, assessment):
    listAccessStudent = []
    for stud in student:
        if stud['Grade Point Average'] >= assessment:
            listAccessStudent.append(stud)      
    
    return listAccessStudent


students = [
    {'name': 'Maria', 'Grade Point Average': 5.6},
    {'name': 'Kutdja', 'Grade Point Average': 4.1},
    {'name': 'Jotaro', 'Grade Point Average': 8.7},
    {'name': 'JoJo', 'Grade Point Average': 1.3},
    {'name': 'John', 'Grade Point Average': 2.1},
    {'name': 'Hellen', 'Grade Point Average': 5.3},
    {'name': 'Memchik', 'Grade Point Average': 9.6},
    {'name': 'Mara', 'Grade Point Average': 7.0},
    {'name': 'Marluba', 'Grade Point Average': 1.5},
    {'name': 'Mark', 'Grade Point Average': 5.0},
]

assessment = 5.0
print(assessmentStudent(students, assessment))