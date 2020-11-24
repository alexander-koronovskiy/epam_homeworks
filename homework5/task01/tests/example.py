from task01.shedule import *

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")

print(teacher.last_name)  # Daniil
print(student.first_name)  # Petrov

# expired_homework = teacher.create_homework("Learn functions", 0)
# expired_homework.created  # Example: 2019-05-26 16:44:30.688762
# expired_homework.deadline  # 0:00:00
# expired_homework.text  # 'Learn functions'

# create function from method and use it
# create_homework_too = teacher.create_homework
# oop_homework = create_homework_too("create 2 simple classes", 5)
# oop_homework.deadline  # 5 days, 0:00:00

hw = Homework("create 2 simple classes", "5 days, 0:00:00")

print(student.do_homework(hw))
print(student.do_homework(hw))  # You are late
