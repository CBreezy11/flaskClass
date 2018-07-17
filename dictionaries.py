student = {'name': 'Jose',
            'school': 'computing',
            'grades': (66, 77, 88)
            }

student_list = [
        {'name': 'John', 'grades': (87, 98, 67)},
        {'name': 'Casey', 'grades': (87, 87, 74)},
        {'name': 'Kevin', 'grades': (98, 95, 91)}
]
def avg_grade(data):
    return (sum(data['grades'])) / (len(data['grades']))

def class_avg(data):
    total = 0
    for student in data:
        total += avg_grade(stud)
    return total / len(data)
        


print("%.2f" % class_avg(student_list))