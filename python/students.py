#001-004
lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90,0]
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

students = [lloyd, alice, tyler]

for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]

#005 AVERAGE NUMBER
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

print average([6,2,4,9,8])

#006-009 GRADE CALCULATOR
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

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])

  # Homework worth 10%, quizzes worth 30%, tests worth 60%
  homework = homework * 0.10
  quizzes = quizzes * 0.30
  tests = tests * 0.60
  return homework + quizzes + tests

def get_letter_grade(score):
  if score >= 90:
    return 'A'
  elif score >= 80:
    return 'B'
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return 'D'
  else:
    return 'F'

print "LLOYD - Score: " + str(get_average(lloyd)) + ", Grade: " + get_letter_grade(get_average(lloyd))
print "ALICE - Score: " + str(get_average(alice)) + ", Grade: " + get_letter_grade(get_average(alice))
print "TYLER - Score: " + str(get_average(tyler)) + ", Grade: " + get_letter_grade(get_average(tyler))

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [alice, lloyd, tyler]

print "CLASS - Score: " + str(get_class_average(students)) + ", Grade: " + str(get_letter_grade(get_class_average(students)))
