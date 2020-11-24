from task01.shedule import *

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")
assert teacher.last_name == "Shadrin"
assert student.first_name == "Roman"

expired_homework = teacher.create_homework("Learn functions", 0)
assert expired_homework.text == "Learn functions"
print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
print(expired_homework.deadline)  # 0:00:00

# create function from method and use it
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)
print(oop_homework.deadline)  # 5 days, 0:00:00
