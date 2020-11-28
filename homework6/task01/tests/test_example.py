"""
User.get_created_instances()  # 0
user, _, _ = User(), User(), User()
user.get_created_instances()  # 3
user.reset_instances_counter()  # 3
"""

from task01.method_adds import get_created_instances, reset_instance_counter


@get_created_instances
@reset_instance_counter
class User:
    pass


user, _, _ = User(), User(), User()


def test_decor():
    assert User.calls == 3
