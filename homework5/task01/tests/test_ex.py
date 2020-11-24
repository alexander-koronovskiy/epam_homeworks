from task01.shedule import *

# Test 1 parameters
teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")

# Test 2 parameters
expired_homework = teacher.create_homework("Learn functions", 0)
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)


def test_names(teacher=teacher, student=student):
    """
    test for correct field broadcasting in Teacher and Student Classes
    """
    assert teacher.last_name == "Shadrin"
    assert student.first_name == "Roman"


def test_hw_parameters():
    """
    test for correct field broadcasting in Homework Class
    """
    assert expired_homework.text == "Learn functions"
    assert str(expired_homework.created) == "2020-11-23 19:15:32"

    assert str(expired_homework.deadline) == "2020-11-23 19:15:32"
    assert str(oop_homework.deadline) == "2020-11-28 19:15:32"


def test_student_hw():
    assert student.do_homework(oop_homework) == ""
    assert student.do_homework(expired_homework) == "You are late"
