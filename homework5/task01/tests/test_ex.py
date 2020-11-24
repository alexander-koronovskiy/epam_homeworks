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
    test for correct methods work in Homework Class
    """
    assert expired_homework.text == "Learn functions"
    assert expired_homework.deadline < datetime.now()
    assert oop_homework.deadline > datetime.now()


def test_student_hw():
    """
    test for correct methods work in Class 'Student'
    """
    assert student.do_homework(oop_homework) == ""
    assert student.do_homework(expired_homework) == "You are late"
