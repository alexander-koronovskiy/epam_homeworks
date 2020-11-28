from task01.method_adds import countcalls


def instances_counter(cls):
    """Some code"""
    return cls


@countcalls
class User:
    pass


if __name__ == "__main__":
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
