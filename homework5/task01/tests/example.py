from task01.shedule import *

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")
expired_homework = teacher.create_homework("Learn functions", 0)


def check_names(teacher, student):
    assert teacher.last_name == "Shadrin"
    assert student.first_name == "Roman"


def check_hw_parameters():
    assert expired_homework.text == "Learn functions"
    assert str(expired_homework.created) == "2020-11-23 19:15:32"
    assert str(expired_homework.deadline) == "2020-11-23 19:15:32"


# create function from method and use it
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)

print("oop_homework.deadline", oop_homework.deadline)  # 5 days, 0:00:00

print("student.do_homework check", student.do_homework(oop_homework))
print(
    "student.do_homework check", student.do_homework(expired_homework)
)  # You are late
