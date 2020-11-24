from task01.shedule import *

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")
assert teacher.last_name == "Shadrin"
assert student.first_name == "Roman"

expired_homework = teacher.create_homework("Learn functions", 0)
assert expired_homework.text == "Learn functions"
print(
    "expired_homework.created", expired_homework.created
)  # Example: 2019-05-26 16:44:30.688762
print("expired_homework.deadline", expired_homework.deadline)  # 0:00:00

# create function from method and use it
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)
print("oop_homework.deadline", oop_homework.deadline)  # 5 days, 0:00:00

print("student.do_homework check", student.do_homework(oop_homework))
print(
    "student.do_homework check", student.do_homework(expired_homework)
)  # You are late

date_select = datetime.strptime("2011-12-1", "%Y-%m-%d")
delta = timedelta(days=1)
target_date = date_select + delta

print(date_select, delta, target_date)
